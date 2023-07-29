import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import Testdata
from Testdata import landing_data
from Testdata.landing_data import Page
from pageobjects import careerinterest, careerinterest1, careerinterest2
from pageobjects.Landingpage import lp
from pageobjects.careerinterest import ci
from utility.base_clas import base_clas


class Testing(base_clas):

    def test_e2end(self, getdata):
        
        log = self.getloggr()

        landing = lp(self.driver)

        landing.signin_wait()

        landing.sign_button().click()

        landing.user_name_wait()

        landing.user_name().send_keys(getdata["uname"])

        log.info("username entered")

        landing.pass_wd().send_keys(getdata["passwd"])

        log.info("Passwd entered")

        landing.submit_button().click()

        landing.take_quiz_wait()

        careerinterest = landing.take_quiz()

        log.info("take new quiz")

        # print("view result")

        # self.driver.find_element(By.XPATH, "//a[@title='Link to View results for Job Ideas Quiz']").click()

        # time.sleep(6)

        # self.driver.find_element(By.XPATH, "//button[(text()='take Job Ideas Quiz again')]").click()

        # time.sleep(5)

        careerinterest.q1_wait()

        careerinterest.quest1().click()

        careerinterest.quest2().click()

        careerinterest.quest3().click()

        careerinterest.quest4().click()

        careerinterest.quest5().click()

        self.next_wait()

        self.next_butn().click()

        log.info("Page 1 saved")

        careerinterest.q6_wait()

        careerinterest.quest6().click()

        self.driver.find_element(By.XPATH, "//div[contains(@class,'content__helper-menu')]/a[2]").click()

        time.sleep(3)

    @pytest.fixture(params=Page.datavalue)
    def getdata(self, request):
        return request.param








"""
    @pytest.fixture(params=Page.gettestdata_full())
    def getdata(self, request):
        return request.param
"""

"""
    @pytest.fixture(params=Page.gettestdata("Testcase1"))
    def getdata(self, request):
        return request.param
"""
