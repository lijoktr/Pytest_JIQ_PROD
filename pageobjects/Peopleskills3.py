from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


class Ps3:

    def __init__(self, driver):
        self.driver = driver

    ps_q1 = (By.XPATH, "//*[contains(@id,'d8ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    ps_q2 = (By.XPATH, "//*[contains(@id,'daecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    ps_q3 = (By.XPATH, "//*[contains(@id,'f9ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    ps_q4 = (By.XPATH, "//*[contains(@id,'02edb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    ps_q5 = (By.XPATH, "//*[contains(@id,'03edb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    def ps_q1_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((Ps3.ps_q1)))

    def ps_quest1(self):
        return self.driver.find_element(*Ps3.ps_q1)

    def ps_quest2(self):
        return self.driver.find_element(*Ps3.ps_q2)

    def ps_quest3(self):
        return self.driver.find_element(*Ps3.ps_q3)

    def ps_quest4(self):
        return self.driver.find_element(*Ps3.ps_q4)

    def ps_quest5(self):
        return self.driver.find_element(*Ps3.ps_q5)

