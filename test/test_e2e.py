import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from selenium.webdriver.common.by import By



#@pytest.mark.usefixtures("setup")
from utility.base_clas import base_clas


class Testing(base_clas):

    def test_e2end(self):


        print("url is ", self.driver.current_url)
        time.sleep(140)

        print("sign in")

        self.driver.find_element(By.XPATH, "//div[@class='branded-masthead__content']/div[2]/a").click()


        #self.driver.find_element(By.XPATH, "//div[@class='branded-masthead__content']/div[2]/a").click()

        time.sleep(4)

        print("email")

        self.driver.find_element(By.XPATH, "//input[@name='Email Address']").send_keys("")

        time.sleep(0)

        print("password")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'password')]").send_keys("")

        time.sleep(0)

        print("submit")

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(6)

        print("take quiz new")

        self.driver.find_element(By.XPATH, "//a[@title='Link to Take Job Ideas Quiz']").click()

        #print("view result")

        #self.driver.find_element(By.XPATH, "//a[@title='Link to View results for Job Ideas Quiz']").click()

        #time.sleep(6)

        #self.driver.find_element(By.XPATH, "//button[(text()='take Job Ideas Quiz again')]").click()

        # time.sleep(5)

        time.sleep(7)

        print("Career interests : question 1 below")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'33bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[3]/div/label/span[1]/span").click()

        time.sleep(0)

        print("Career interests : question 2 below")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'39bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

        time.sleep(0)

        print("Career interests : question 3 below")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'3bbd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[2]/div/label/span[1]/span").click()

        time.sleep(0)

        print("Career interests : question 4 below")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'42bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

        time.sleep(0)

        print("Career interests : question 5 below")

        self.driver.find_element(By.XPATH, "//*[contains(@id,'44bd84a0-edd2-ed11-a7c7-0022481b53e3')]/div/div[1]/div/label/span[1]/span").click()

        time.sleep(3)

        print("Career interests : next")

        self.driver.find_element(By.XPATH, "//*[contains(@title,'Link to next')]").click()

        time.sleep(500)













