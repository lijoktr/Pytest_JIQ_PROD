from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# from Testdata.career_interestdata import ci


class ci2:

    def __init__(self, driver):
        self.driver = driver

    q1 = (By.XPATH, "//*[contains(@id,'21f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q2 = (By.XPATH, "//*[contains(@id,'31f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q3 = (By.XPATH, "//*[contains(@id,'34f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q4 = (By.XPATH, "//*[contains(@id,'3cf9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q5 = (By.XPATH, "//*[contains(@id,'3ff9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q6 = (By.XPATH, "//*[contains(@id,'4af9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q7 = (By.XPATH, "//*[contains(@id,'50f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[1]/div/label/span[1]/span")

    q8 = (By.XPATH, "//*[contains(@id,'54f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[1]/div/label/span[1]/span")

    q9 = (By.XPATH, "//*[contains(@id,'55f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[1]/div/label/span[1]/span")

    q10 = (By.XPATH, "//*[contains(@id,'56f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    q11 = (By.XPATH, "//*[contains(@id,'59f9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[2]/div/label/span[1]/span")

    q12 = (By.XPATH, "//*[contains(@id,'5af9d7c4-5800-ee11-8f6d-0022481b547c')]/div/div[3]/div/label/span[1]/span")

    # next = (By.XPATH, "//*[contains(@title,'Link to next')]")

    def q1_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci2.q1)))

    def quest1(self):
        return self.driver.find_element(*ci2.q1)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[3]/div/label/span[1]/span").click()

    def quest2(self):
        return self.driver.find_element(*ci2.q2)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest3(self):
        return self.driver.find_element(*ci2.q3)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest4(self):
        return self.driver.find_element(*ci2.q4)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def quest5(self):
        return self.driver.find_element(*ci2.q5)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def q6_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci2.q6)))

    def quest6(self):
        return self.driver.find_element(*ci2.q6)
        # self.driver.find_element_by_xpath("//*[contains(@id,'4bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest7(self):
        return self.driver.find_element(*ci2.q7)

    def quest8(self):
        return self.driver.find_element(*ci2.q8)

    def quest9(self):
        return self.driver.find_element(*ci2.q9)

    def quest10(self):
        return self.driver.find_element(*ci2.q10)

    def q11_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((ci2.q11)))

    def quest11(self):
        return self.driver.find_element(*ci2.q11)

    def quest12(self):
        return self.driver.find_element(*ci2.q12)


