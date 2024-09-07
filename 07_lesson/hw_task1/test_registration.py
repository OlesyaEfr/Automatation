import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from registration_page import RegistrationPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    submit_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)  # Scroll to the button
    driver.execute_script("arguments[0].click();", submit_button)



    red = '#842029'  # '#FF0000'
    green = '#0f5132'  # '#008000'

    check_color_by_class(registration_page, "alert-danger", red)
    check_color_by_class(registration_page, "alert-success", green)


def check_color_by_class(page, class_name, expected_color):
    field = page.get_element_by_class(class_name)
    actual_color = Color.from_string(field.value_of_css_property('color')).hex
    print(f"Expected color {expected_color}, but got {actual_color}")
    assert actual_color == expected_color