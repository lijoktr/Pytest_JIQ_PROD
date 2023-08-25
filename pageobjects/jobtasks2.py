from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


class jt2:

    def __init__(self, driver):
        self.driver = driver

    jt_q1 = (By.XPATH, "//*[contains(@id,'ddecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    jt_q2 = (By.XPATH, "//*[contains(@id,'e0ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    jt_q3 = (By.XPATH, "//*[contains(@id,'e1ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    jt_q4 = (By.XPATH, "//*[contains(@id,'e6ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    jt_q5 = (By.XPATH, "//*[contains(@id,'ececb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    jt_q6 = (By.XPATH, "//*[contains(@id,'edecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    jt_q7 = (By.XPATH, "//*[contains(@id,'f0ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    jt_q8 = (By.XPATH, "//*[contains(@id,'f2ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    jt_q9 = (By.XPATH, "//*[contains(@id,'f3ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    jt_q10 = (By.XPATH, "//*[contains(@id,'f4ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    jt_q11 = (By.XPATH, "//*[contains(@id,'feecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    jt_q12 = (By.XPATH, "//*[contains(@id,'00edb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    jt_q13 = (By.XPATH, "//*[contains(@id,'01edb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    def jt_q1_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((jt2.jt_q1)))

    def jt_quest1(self):
        return self.driver.find_element(*jt2.jt_q1)

    def jt_quest2(self):
        return self.driver.find_element(*jt2.jt_q2)

    def jt_quest3(self):
        return self.driver.find_element(*jt2.jt_q3)

    def jt_quest4(self):
        return self.driver.find_element(*jt2.jt_q4)

    def jt_quest5(self):
        return self.driver.find_element(*jt2.jt_q5)

    def jt_q6_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((jt2.jt_q6)))

    def jt_quest6(self):
        return self.driver.find_element(*jt2.jt_q6)

    def jt_quest7(self):
        return self.driver.find_element(*jt2.jt_q7)

    def jt_quest8(self):
        return self.driver.find_element(*jt2.jt_q8)

    def jt_quest9(self):
        return self.driver.find_element(*jt2.jt_q9)

    def jt_quest10(self):
        return self.driver.find_element(*jt2.jt_q10)

    def jt_q11_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((jt2.jt_q11)))

    def jt_quest11(self):
        return self.driver.find_element(*jt2.jt_q11)

    def jt_quest12(self):
        return self.driver.find_element(*jt2.jt_q12)

    def jt_quest13(self):
        return self.driver.find_element(*jt2.jt_q13)


