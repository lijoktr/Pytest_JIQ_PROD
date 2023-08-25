
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec


class We4:

    def __init__(self, driver):
        self.driver = driver

    we_q1 = (By.XPATH, "//*[contains(@id,'d9ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q2 = (By.XPATH, "//*[contains(@id,'dbecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    we_q3 = (By.XPATH, "//*[contains(@id,'dfecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q4 = (By.XPATH, "//*[contains(@id,'e2ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q5 = (By.XPATH, "//*[contains(@id,'e3ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q6 = (By.XPATH, "//*[contains(@id,'e4ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    we_q7 = (By.XPATH, "//*[contains(@id,'e8ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q8 = (By.XPATH, "//*[contains(@id,'e9ecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[3]/span/label/span[1]/span")

    we_q9 = (By.XPATH, "//*[contains(@id,'eaecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    we_q10 = (By.XPATH, "//*[contains(@id,'ebecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    we_success = (By.CSS_SELECTOR, "[class*='notice--positive']")

    we_q11 = (By.XPATH, "//*[contains(@id,'efecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[2]/span/label/span[1]/span")

    we_q12 = (By.XPATH, "//*[contains(@id,'fbecb72c-d31b-ee11-8f6d-0022481b5881')]/div/div[1]/span/label/span[1]/span")

    submit_button = (By.XPATH, "//button[@title='Link to Submit']")

    Tq_again = (By.XPATH, "//button[text()='take Job Ideas Quiz again']")

    def we_q1_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((We4.we_q1)))

    def we_quest1(self):
        return self.driver.find_element(*We4.we_q1)

    def we_quest2(self):
        return self.driver.find_element(*We4.we_q2)

    def we_quest3(self):
        return self.driver.find_element(*We4.we_q3)

    def we_quest4(self):
        return self.driver.find_element(*We4.we_q4)

    def we_quest5(self):
        return self.driver.find_element(*We4.we_q5)

    def we_q6_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((We4.we_q6)))

    def we_quest6(self):
        return self.driver.find_element(*We4.we_q6)

    def we_quest7(self):
        return self.driver.find_element(*We4.we_q7)

    def we_quest8(self):
        return self.driver.find_element(*We4.we_q8)

    def we_quest9(self):
        return self.driver.find_element(*We4.we_q9)

    def we_quest10(self):
        return self.driver.find_element(*We4.we_q10)

    def we_q11_wait(self):
        Wait = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((We4.we_q11)))

    def we_success_message(self):
        return self.driver.find_element(*We4.we_success)

    def we_quest11(self):
        return self.driver.find_element(*We4.we_q11)

    def we_quest12(self):
        return self.driver.find_element(*We4.we_q12)

    def submit_wait(self):
        wait = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(We4.submit_button))

    def submit(self):
        return self.driver.find_element(*We4.submit_button)

    def tq_again_wait(self):
        wait = WebDriverWait(self.driver,5).until((ec.visibility_of_element_located((We4.Tq_again))))

    def take_quiz_again(self):
        button = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(We4.Tq_again))
        button.click()


