import inspect

import logging

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup")
class base_clas:

    next = (By.XPATH, "//*[contains(@title,'Link to next')]")

    def getloggr(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)

        return logger

    def next_wait(self):
        Wait = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((base_clas.next)))

    def next_butn(self):
        return self.driver.find_element(*base_clas.next)
        # self.driver.find_element(By.XPATH, "//*[contains(@title,'Link to next')]").click()