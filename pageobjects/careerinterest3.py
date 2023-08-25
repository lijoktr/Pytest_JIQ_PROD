from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# from Testdata.career_interestdata import ci


class ci3:

    def __init__(self, driver):
        self.driver = driver

    q1 = (By.XPATH, "//*[contains(@id,'d7ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    q2 = (By.XPATH, "//*[contains(@id,'dcecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    q3 = (By.XPATH, "//*[contains(@id,'deecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    q4 = (By.XPATH, "//*[contains(@id,'e5ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    q5 = (By.XPATH, "//*[contains(@id,'e7ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    q6 = (By.XPATH, "//*[contains(@id,'eeecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    q7 = (By.XPATH, "//*[contains(@id,'f1ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    q8 = (By.XPATH, "//*[contains(@id,'f5ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    q9 = (By.XPATH, "//*[contains(@id,'f6ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    q10 = (By.XPATH, "//*[contains(@id,'f8ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    q11 = (By.XPATH, "//*[contains(@id,'fcecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    q12 = (By.XPATH, "//*[contains(@id,'fdecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    # next = (By.XPATH, "//*[contains(@title,'Link to next')]")

    def q1_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci3.q1)))

    def quest1(self):
        return self.driver.find_element(*ci3.q1)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[3]/span/label/span[1]/span").click()

    def quest2(self):
        return self.driver.find_element(*ci3.q2)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/span/label/span[1]/span").click()

    def quest3(self):
        return self.driver.find_element(*ci3.q3)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/span/label/span[1]/span").click()

    def quest4(self):
        return self.driver.find_element(*ci3.q4)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/span/label/span[1]/span").click()

    def quest5(self):
        return self.driver.find_element(*ci3.q5)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/span/label/span[1]/span").click()

    def q6_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci3.q6)))

    def quest6(self):
        return self.driver.find_element(*ci3.q6)
        # self.driver.find_element_by_xpath("//*[contains(@id,'4bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/span/label/span[1]/span").click()

    def quest7(self):
        return self.driver.find_element(*ci3.q7)

    def quest8(self):
        return self.driver.find_element(*ci3.q8)

    def quest9(self):
        return self.driver.find_element(*ci3.q9)

    def quest10(self):
        return self.driver.find_element(*ci3.q10)

    def q11_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci3.q11)))

    def quest11(self):
        return self.driver.find_element(*ci3.q11)

    def quest12(self):
        return self.driver.find_element(*ci3.q12)


