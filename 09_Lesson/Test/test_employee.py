import pytest
import requests
from Pages.employee import Employee
from Pages.Database import DataBase

api = Employee("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

#Получаем список соудников из БД и через АПИ, после чего сравниваем их
def test_get_list_of_employers():
    #Создаем компанию в БД
    db.create_company('Test_Efr', 'cool_company')
    #Получаем id созданной компании
    max_id = db.last_company_id()
    #Добавляем сотрудника в компанию
    db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
    #Получаем список сотрудников из последней созданной компании из БД
    db_employer_list = db.get_list_employer(max_id)
    #Получаем список сотрудников из последней созданной компании через АПИ
    api_employer_list = api.get_list_employee_company(max_id)
    #Сравниваем списки сотрудников полученных из БД и через АПИ
    assert len(db_employer_list) == len(api_employer_list)
    #Удаляем сотрудника компании, иначе компания не удалится
    response = (api.get_list_employee_company(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    #Удаляем последнюю созданную компанию из БД
    db.delete(max_id)

#Добавить сотрудника в БД и сравнить с АПИ имя, статус и фамилию
def test_add_new_employer():
    db.create_company('Olesya adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
    response = (api.get_list_employee_company(max_id))[0]
    employer_id = response["id"]
    #Сравниваем id компании
    assert response["companyId"] == max_id
    #Сравниваем имя сотрудника
    assert response["firstName"] == "Olesya"
    #Статус сотрудника д.б. True
    assert response["isActive"] == True
    #Сравниваем фамилию
    assert response["lastName"] == "Efrem"
    #Удаляем сотрудника
    db.delete_employer(employer_id)
    #Удаляем компанию
    db.delete(max_id)

#Сравниваем информацию о сотруднике из АПИ с измененной информацией в БД
def test_update_user_info():
    db.create_company('New company', 'new_test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Olesya", "Efrem", 8002000600)
    employer_id = db.get_employer_id(max_id)[0]
    db.update_employer_info("Lesya", employer_id)
    #Сравниваем инфо
    get_api_info = (api.get_info_for_employee(employer_id)).json()
    assert get_api_info["firstName"] == "Lesya"
    assert get_api_info["lastName"] == "Efrem"
    assert get_api_info["isActive"] == True
    #Удаляем сотрудника
    db.delete_employer(employer_id)
    #Удаляем компанию
    db.delete(max_id)
