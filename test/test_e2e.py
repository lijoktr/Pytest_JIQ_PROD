import sys

import pytest
import time
from selenium.webdriver.common.by import By

from Testdata.landing_data import Page

from pageobjects.Landingpage import lp
from pageobjects.Peopleskills1 import Ps1
from pageobjects.Peopleskills3 import Ps3
from pageobjects.Peopleskills4 import Ps4
from pageobjects.Peopleskills5 import Ps5
from pageobjects.Result import Result_page

from pageobjects.careerinterest1 import ci1
from pageobjects.careerinterest2 import ci2
from pageobjects.careerinterest3 import ci3
from pageobjects.careerinterest4 import ci4
from pageobjects.careerinterest5 import ci5
from pageobjects.jobtasks1 import jt1
from pageobjects.jobtasks2 import jt2
from pageobjects.jobtasks3 import jt3
from pageobjects.jobtasks4 import jt4
from pageobjects.jobtasks5 import jt5
from pageobjects.workenvironment1 import We1
from pageobjects.workenvironment3 import We3
from pageobjects.workenvironment4 import We4
from pageobjects.workenvironment5 import We5
from utility.base_clas import base_clas

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


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

        log.info("submit")

        landing.take_quiz_wait()

        landing.take_quiz().click()

        log.info("take new quiz")

        # log.info("view result")

        # self.driver.find_element(By.XPATH, "//a[@title='Link to View results for Job Ideas Quiz']").click()

        # time.sleep(6)

        # self.driver.find_element(By.XPATH, "//button[(text()='take Job Ideas Quiz again')]").click()

        # time.sleep(5)

        for x in range(1, 6):

            if x == 1:
                career_interest = ci1(self.driver)
                job_tasks = jt1(self.driver)
                people_skills = Ps1(self.driver)
                work_environment = We1(self.driver)

            elif x == 2:
                career_interest = ci2(self.driver)
                job_tasks = jt2(self.driver)
                people_skills = Ps1(self.driver)
                work_environment = We1(self.driver)

            elif x == 3:
                career_interest = ci3(self.driver)
                job_tasks = jt3(self.driver)
                people_skills = Ps3(self.driver)
                work_environment = We3(self.driver)

            elif x == 4:
                career_interest = ci4(self.driver)
                job_tasks = jt4(self.driver)
                people_skills = Ps4(self.driver)
                work_environment = We4(self.driver)

            elif x == 5:
                career_interest = ci5(self.driver)
                job_tasks = jt5(self.driver)
                people_skills = Ps5(self.driver)
                work_environment = We5(self.driver)

            else:
                career_interest = None
                job_tasks = None
                people_skills = None
                work_environment = None

            # log.info("view result")

            # self.driver.find_element(By.XPATH, "//a[@title='Link to View results for Job Ideas Quiz']").click()

            # time.sleep(6)

            # self.driver.find_element(By.XPATH, "//button[(text()='take Job Ideas Quiz again')]").click()

            # time.sleep(5)

            career_interest.q1_wait()

            career_interest.quest1().click()

            career_interest.quest2().click()

            career_interest.quest3().click()

            career_interest.quest4().click()

            career_interest.quest5().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 1 saved")

            career_interest.q6_wait()

            career_interest.quest6().click()

            career_interest.quest7().click()

            career_interest.quest8().click()

            career_interest.quest9().click()

            career_interest.quest10().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 2 saved")

            career_interest.q11_wait()

            career_interest.quest11().click()

            career_interest.quest12().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 3 saved")

            job_tasks.jt_q1_wait()

            job_tasks.jt_quest1().click()

            job_tasks.jt_quest2().click()

            job_tasks.jt_quest3().click()

            job_tasks.jt_quest4().click()

            job_tasks.jt_quest5().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 4 saved")

            job_tasks.jt_q6_wait()

            job_tasks.jt_quest6().click()

            job_tasks.jt_quest7().click()

            job_tasks.jt_quest8().click()

            job_tasks.jt_quest9().click()

            job_tasks.jt_quest10().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 5 saved")

            job_tasks.jt_q11_wait()

            job_tasks.jt_quest11().click()

            job_tasks.jt_quest12().click()

            job_tasks.jt_quest13().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 6 saved")

            people_skills.ps_q1_wait()

            people_skills.ps_quest1().click()

            people_skills.ps_quest2().click()

            people_skills.ps_quest3().click()

            people_skills.ps_quest4().click()

            people_skills.ps_quest5().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 7 saved")

            work_environment.we_q1_wait()

            work_environment.we_quest1().click()

            work_environment.we_quest2().click()

            work_environment.we_quest3().click()

            work_environment.we_quest4().click()

            work_environment.we_quest5().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 8 saved")

            work_environment.we_q6_wait()

            work_environment.we_quest6().click()

            work_environment.we_quest7().click()

            work_environment.we_quest8().click()

            work_environment.we_quest9().click()

            work_environment.we_quest10().click()

            self.next_wait()

            self.next_butn().click()

            log.info("Page 9 saved")

            work_environment.we_q11_wait()

            alertText = work_environment.we_success_message().text

            assert ("You have saved your quiz answers" in alertText)

            log.info(alertText)

            work_environment.we_quest11().click()

            work_environment.we_quest12().click()

            work_environment.submit_wait()

            work_environment.submit().click()

            log.info("Quiz submitted")

            wait = WebDriverWait(self.driver, 10)

            result = Result_page(self.driver)

            try:
                log.info("retake_wait")
                wait = result.retake_wait()
                log.info("take_quiz_again")
                result.retake().click()

            except:
                log.info("max limit(5) of taking quiz reached.")
<<<<<<< HEAD

                # Find the table element
                table = result.table()  # Replace with the actual table locator

                log.info("table located")

                rows = result.row_locate(table)

                actual_data_column_3 = []
                actual_data_column_4 = []

                log.info("Loop through each row and extract the data from the 3rd and 4th column")
                for row in rows:
                    cells = result.column_locate(row)

                    if len(cells) > 2:
                        data_column_3 = cells[2].text
                        data_column_4 = cells[3].text
                        actual_data_column_3.append(data_column_3)
                        actual_data_column_4.append(data_column_4)
                # log.info("actual data stored")

                # Expected data that you want to verify against
                expected_data_column_3 = ["Plumber", "Sports Coach", "Animal Attendant",
                                          "Plasterer", "Veterinary Nurse", "Nurse", "Bricklayer", "Factory Worker",
                                          "Electrician", "Painter and Decorator"]  # Replace with actual expected data
                expected_data_column_4 = ["85%", "83%", "82%", "80%", "80%", "75%", "74%", "74%", "70%",
                                          "70%"]  # Replace with actual expected data

                # log.info("expected data stored")
                log.info(actual_data_column_3)
                log.info(actual_data_column_4)

                # Verify if the actual data from the 2nd and 3rd columns match the expected data
                if actual_data_column_3 == expected_data_column_3 and actual_data_column_4 == expected_data_column_4:
                    log.info("Data verification successful for the 2nd and 3rd columns.")
                else:
                    log.info("Data verification failed for the 2nd and 3rd columns.")
                return
=======

                # Find the table element
                table = result.table()  # Replace with the actual table locator

                log.info("table located")

                rows = result.row_locate(table)

                actual_data_column_3 = []
                actual_data_column_4 = []

                log.info("Loop through each row and extract the data from the 3rd and 4th column")
                for row in rows:
                    cells = result.column_locate(row)

                    if len(cells) > 2:
                        data_column_3 = cells[2].text
                        data_column_4 = cells[3].text
                        actual_data_column_3.append(data_column_3)
                        actual_data_column_4.append(data_column_4)
                # log.info("actual data stored")

                # Expected data that you want to verify against
                expected_data_column_3 = ["Plumber", "Sports Coach", "Animal Attendant",
                                          "Plasterer", "Veterinary Nurse", "Nurse", "Bricklayer", "Factory Worker",
                                          "Electrician", "Painter and Decorator"]  # Replace with actual expected data
                expected_data_column_4 = ["85%", "83%", "82%", "80%", "80%", "75%", "74%", "74%", "70%",
                                          "70%"]  # Replace with actual expected data

                # log.info("expected data stored")
                log.info(actual_data_column_3)
                log.info(actual_data_column_4)

                # Verify if the actual data from the 2nd and 3rd columns match the expected data
                if actual_data_column_3 == expected_data_column_3 and actual_data_column_4 == expected_data_column_4:
                    log.info("Data verification successful for the 2nd and 3rd columns.")
                else:
                    log.info("Data verification failed for the 2nd and 3rd columns.")

                self.driver.quit()
>>>>>>> 5ba2ad54f3ee954d0cbd51cb94064013f6151cd4

    @pytest.fixture(params=Page.datavalue)
    def getdata(self, request):
        return request.param
