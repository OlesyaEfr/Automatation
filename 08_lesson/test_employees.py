from employees import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Olesya"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "Olesya"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Olesya123", "B")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Olesya123"
    assert resp[0]["lastName"] == "B"


def test_get_employee_by_id():
    name = "Olesya"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Olesya123", "Be")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Olesya123"
    assert get_info["lastName"] == "Be"


def test_change_employee_info():
    name = "Olesya"
    descr = "test"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Olesya123", "Ber")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Ber2", "test2@mail.ru")
    assert update["id"] == id_employee
    assert update["email"] == "test2@mail.ru"
