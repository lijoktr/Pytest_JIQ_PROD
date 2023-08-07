from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.careerinterest1 import ci1
from selenium.webdriver.support import expected_conditions as ec


class lp:

    def __init__(self, driver):
        self.driver = driver

    signin = (By.XPATH, "//div[@class='branded-masthead__content']/div[2]/a")
    username = (By.XPATH, "//input[@name='Email Address']")
    passwd = (By.XPATH, "//*[contains(@id,'password')]")
    submitbuttn = (By.CSS_SELECTOR, "button[type='submit']")
    takequiz = (By.XPATH, "//a[@title='Link to Take Job Ideas Quiz']")

    def signin_wait(self):
        Wait = WebDriverWait(self.driver, 160).until(
            ec.visibility_of_element_located((lp.signin)))

    def sign_button(self):
        return self.driver.find_element(*lp.signin)
        # self.driver.find_element(By.XPATH, "//div[@class='branded-masthead__content']/div[2]/a").click()

    def user_name_wait(self):
        Wait = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((lp.username)))

    def user_name(self):
        return self.driver.find_element(*lp.username)
        #self.driver.find_element(By.XPATH, "//input[@name='Email Address']").send_keys("Lijo.mathew+1@careerswales.gov.wales ")

    def pass_wd(self):
        return self.driver.find_element(*lp.passwd)
        #self.driver.find_element(By.XPATH, "//*[contains(@id,'password')]").send_keys("Lijo@sysint1")

    def submit_button(self):
        return self.driver.find_element(*lp.submitbuttn)
        #self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def take_quiz_wait(self):
        Wait = WebDriverWait(self.driver, 6).until(
            ec.visibility_of_element_located((lp.takequiz)))

    def take_quiz(self):
        return self.driver.find_element(*lp.takequiz)
        #self.driver.find_element(By.XPATH, "//a[@title='Link to Take Job Ideas Quiz']").click()




