from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import data
import time
from page_funtions import *

class Cases_test:

    driver = None

    def setup_class(self):

        self.driver = webdriver.Chrome()
        self.driver.get(url=data.url_page)

    def collect_credencials(self):
        login_test = Sauce_funct(self.driver)
        list_username = login_test.collect_usarname()
        list_password = login_test.collect_password()

        for name in list_username:
            print(name.get_property('text'))
        
        
        print(len(list_username))
        print(len(list_password))


    def error_moment(self):
        error_login_test = Sauce_funct(self.driver)
        list_error = error_login_test.collect_error_msj()
        print(list_error)

