import requests
from constants import X_client_URl
import json

path = '/employee/'


class Company:
    def __init__(self,url=X_client_URl):
        self.url = url

# Вызываем последнюю активную компанию
    def last_active_company(self):
        active_params = {'active': 'true'}
        response = requests.get(self.url + '/company', params=active_params)
        return response.json()[-1]['id']   

class Employee:
    def __init__(self,url=X_client_URl):
        self.url = url

# Получить список сотрудников компании
    def get_list_employee_company(self,company_id:int):
        company = {'company': company_id}
        response = requests.get(self.url + path,params= company)
        return response.json()    

# Добавляем сотрудника в компанию
    def add_employee_into_company(self,token:str,body:json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + path, headers=headers,json=body)
        return response.json()    

# Получение информации о сотруднике
    def get_info_for_employee(self,id_employee:int):
        response = requests.get(self.url + path +str(id_employee))
        return response    

# Изменение информации о сотруднике

    def change_info_for_employee(self, token:str, id_employee:int, body:json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(id_employee), headers=headers,json=body)
        return response.json()
        