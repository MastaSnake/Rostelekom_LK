import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome('указать путь к драйверу хром')
    yield driver
    driver.quit()