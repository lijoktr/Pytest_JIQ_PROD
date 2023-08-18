from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Result_page:

    def __init__(self, driver):
        self.driver = driver

    Rv_quiz = (By.XPATH, "//button[text()='take Job Ideas Quiz again']")

    Rv_table = (By.TAG_NAME, 'table')

    Rv_row = (By.TAG_NAME, 'tr')

    Rv_column = (By.TAG_NAME, 'td')

    def retake_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((Result_page.Rv_quiz)))

    def retake(self):
        return self.driver.find_element(*Result_page.Rv_quiz)

    def table(self):
        return self.driver.find_element(*Result_page.Rv_table)

    def row_locate(self, table):
        return table.find_elements(*Result_page.Rv_row)

    def column_locate(self, row):
        return row.find_elements(*Result_page.Rv_column)


