
import pytest
from selenium import webdriver
#from selenium.webdriver.chrome import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://sysint.careerswales.gov.wales/job-ideas-quiz")
    driver.maximize_window()
    request.cls.driver = driver   #instead of return driver
    yield
    driver.close()   #executing last


