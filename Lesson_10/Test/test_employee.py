import allure
import pytest
import requests
from Pages.employee import Employee
from Pages.Database import DataBase

api = Employee("https://x-clients-be.onrender.com")
db = DataBase(
        "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

@allure.epic("x-clients") 
@allure.severity("blocker")
@allure.title("Список сотрудников")
@allure.description("Получаем список соудников из БД и через АПИ, после чего сравниваем их")
@allure.feature("GET")    
def test_get_list_of_employers():
    with allure.step("Создаем компанию в БД"):
        db.create_company('Test_Efr', 'cool_company')
    with allure.step("Получаем id созданной компании"):
        max_id = db.last_company_id()
    with allure.step("Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
    with allure.step("Получаем список сотрудников из последней созданной компании из БД"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("Получаем список сотрудников из последней созданной компании через АПИ"):
        api_employer_list = api.get_list_employee_company(max_id)
    with allure.step("Сравниваем списки сотрудников полученных из БД и через АПИ"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("Удаляем сотрудника компании, чтобы удалить компанию потом"):
        response = (api.get_list_employee_company(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("Удаляем последнюю созданную компанию из БД"):
        db.delete(max_id)

@allure.epic("x-clients") 
@allure.severity("blocker")
@allure.title("Список сотрудников")
@allure.description("Добавить сотрудника в БД и сравнить с данными через АПИ: имя, статус и фамилию")
@allure.feature("ADD")
def test_add_new_employer():
    with allure.step("Создаем компанию в БД"):
        db.create_company('Olesya adding new employer', 'employer')
    with allure.step("Получаем id созданной компании"):
        max_id = db.last_company_id()
    with allure.step("Создаем сотрудника в последней созданной компании"):        
        db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
        response = (api.get_list_employee_company(max_id))[0]
        employer_id = response["id"]
    with allure.step("Сравниваем id компании"):
        assert response["companyId"] == max_id
    with allure.step("Сравниваем имя сотрудника, статус и фамилию"):
        assert response["firstName"] == "Olesya"
        assert response["isActive"] == True
        assert response["lastName"] == "Efrem"
    with allure.step("Удаляем сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем компанию"):
        db.delete(max_id)

@allure.epic("x-clients") 
@allure.severity("blocker")
@allure.title("Список сотрудников")
@allure.description("Сравниваем информацию о сотруднике, полученную через АПИ, с измененной информацией в БД")
@allure.feature("UPDATE")
def test_update_user_info():
    with allure.step("Создаем компанию в БД"):
        db.create_company('New company', 'new_test')
    with allure.step("Получаем id созданной компании"):
        max_id = db.last_company_id()
    with allure.step("Создаем сотрудника в последней созданной компании"):
        db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
        employer_id = db.get_employer_id(max_id)[0]
        db.update_employer_info("Lesya", employer_id)
    with allure.step("Сравниваем данные, полученные из АПИ с измененными"):
        get_api_info = (api.get_info_for_employee(employer_id)).json()
        assert get_api_info["firstName"] == "Lesya"
        assert get_api_info["lastName"] == "Efrem"
        assert get_api_info["isActive"] == True
    with allure.step("Удаляем сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем компанию"):
        db.delete(max_id)
