from case_test import *
from data import *
import time

def run():

    usernames = list()
    passwords = list()

    login_page_test_sauce = Unit_Functions()

    # test 1 : Probar login with credenciales
    login_page_test_sauce.setup_class()
    usernames, passwords = login_page_test_sauce.collect_credencials()

    for keyword in passwords:
        for user in usernames:
            login_page_test_sauce.write_credencials(user, keyword)
            time.sleep(0.5)
            login_page_test_sauce.click_login()
            time.sleep(2)
            current_url = login_page_test_sauce.get_current_url()

            if current_url != str(url_page + inventory_page):
                raise AssertionError(f'Las credenciasles user:{user} password:{keyword} son Incorrectas')
            else:
                print(f'Las credenciasles user:{user} password:{keyword} son Correctas')
                login_page_test_sauce.click_logout()
                

if __name__ == "__main__":
    run()
