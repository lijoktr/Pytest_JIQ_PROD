from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#from Testdata.career_interestdata import ci


class ci:

    def __init__(self, driver):
        self.driver = driver

        q1 = (By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

        q2 = (By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

        q3 = (By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

        q4 = (By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

        q5 = (By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

        q6 = (By.XPATH, "//*[contains(@id,'4bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span")

    #next = (By.XPATH, "//*[contains(@title,'Link to next')]")

    def q1_wait(self):
        Wait = WebDriverWait(self.driver, 7).until(
            ec.visibility_of_element_located((ci.q1)))

    def quest1(self):
        return self.driver.find_element(*ci.q1)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[3]/div/label/span[1]/span").click()

    def quest2(self):
        return self.driver.find_element(*ci.q2)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest3(self):
        return self.driver.find_element(*ci.q3)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest4(self):
        return self.driver.find_element(*ci.q4)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def quest5(self):
        return self.driver.find_element(*ci.q5)
        # self.driver.find_element(By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def q6_wait(self):
        Wait = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((ci.q6)))

    def quest6(self):
        return self.driver.find_element(*ci.q6)
        # self.driver.find_element_by_xpath("//*[contains(@id,'4bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()




"""
    def q1_wait(self):
        Wait = WebDriverWait(self.driver, 7).until(
            ec.visibility_of_element_located((ci.q1)))

    def quest1(self):
        return self.driver.find_element(*ci.q1)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[3]/div/label/span[1]/span").click()

    def quest2(self):
        return self.driver.find_element(*ci.q2)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest3(self):
        return self.driver.find_element(*ci.q3)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

    def quest4(self):
        return self.driver.find_element(*ci.q4)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def quest5(self):
        return self.driver.find_element(*ci.q5)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

    def q6_wait(self):
        Wait = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((ci.q6)))

    def quest6(self):
        return self.driver.find_element(*ci.q6)
        #self.driver.find_element_by_xpath("//*[contains(@id,'4bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()
"""

