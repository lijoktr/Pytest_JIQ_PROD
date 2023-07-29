import pytest

import Testdata
from Testdata import landing_data
from Testdata.landing_data import Page
from pageobjects import careerinterest
from pageobjects.Landingpage import lp
from pageobjects.careerinterest import ci
from utility.base_clas import base_clas
import time


class Testing(base_clas):

    def test_sysint(self, getdata):

        log = self.getloggr()

        landing = lp(self.driver)

        landing.signin_wait()

        #landing.sign_button().click()

        landing.user_name_wait()

        landing.user_name().send_keys(getdata["uname"])

        log.info("username entered")

        landing.pass_wd().send_keys(getdata["passwd"])

        log.info("Passwd entered")

        landing.submit_button().click()

        time.sleep(10)

    @pytest.fixture(params = Page.datavalue)
    def getdata(self, request):
        return request.param