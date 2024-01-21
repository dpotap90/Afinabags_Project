import allure
import faker
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Начало и конец теста
@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

# Запуск браузера
@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

# Скриншот Allure при падении теста
@pytest.fixture(scope='function')
def screenshot_allure(request, driver):
    yield
    outcome = request.session.testsfailed
    if outcome > 0:
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot_{request.function.__name__}", attachment_type=allure.attachment_type.PNG)

# Генерации тестовых данных
@pytest.fixture(scope='function')
def faker_instance():
    fake = faker.Faker()
    return fake
