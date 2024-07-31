import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.localizadores import *

class Sauce_funct:

    def __init__(self, driver):
        self.driver = driver

    # test login page
    def set_username(self, usarname):
        self.driver.find_element(*username_field).send_keys(usarname)

    def set_password(self, password):
        self.driver.find_element(*password_field).send_keys(password)

    def press_button(self):
        self.driver.find_element(*button_field).click()

    def collect_usarname(self):
        return self.driver.find_elements(*examp_usaername_field)
    
    def collect_password(self):
        return self.driver.find_elements(*examp_password_field)
    
    def collect_error_msj(self):
        return self.driver.find_element(*error_msg_field)