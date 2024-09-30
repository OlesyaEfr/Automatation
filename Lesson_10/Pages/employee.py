import requests
import json
import allure

path = '/employee/'

class Employee:
    def __init__(self, url='https://x-clients-be.onrender.com'):
        self.url = url

    @allure.step("Получить список сотрудников компании") 
    def get_list_employee_company(self,company_id:int):
        company = {'company': company_id}
        response = requests.get(
            self.url + path, params = company)
        return response.json()    

    @allure.step("Добавляем сотрудника в компанию")
    def add_employee_into_company(self,token:str,body:json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + path, headers=headers,json=body)
        return response.json()    

    @allure.step("Получение информации о сотруднике")
    def get_info_for_employee(self,id_employee:int):
        response = requests.get(self.url + path +str(id_employee))
        return response    

    @allure.step("Изменение информации о сотруднике")
    def change_info_for_employee(self, token:str, id_employee:int, body:json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(id_employee), headers=headers,json=body)
        return response.json()
