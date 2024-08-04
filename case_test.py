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
        usarname_html_txt = login_test.collect_usarname().text
        password_html_txt = login_test.collect_password().text

        list_username = usarname_html_txt.split('\n')
        list_username.pop(0)

        list_password = password_html_txt.split('\n')
        list_password.pop(0)
     
        print(list_username)
        print(list_password)

        return list_username, list_password
    
    def click_login(self):
        button_login_text = Sauce_funct(self.driver)
        button_login_text.press_button()

    def wait_for_error(self):
        error_msg = Sauce_funct(self.driver)
        error_msg.wait_for_error_msg()
        

        
    def error_moment(self):
        error_login_test = Sauce_funct(self.driver)
        list_error = error_login_test.collect_error_msj()
        print(list_error)

