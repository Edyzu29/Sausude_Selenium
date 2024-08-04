from case_test import *


def run():
    login_page_test_sauce = Cases_test()
    login_page_test_sauce.setup_class()
    login_page_test_sauce.collect_credencials()
    login_page_test_sauce.click_login()
    login_page_test_sauce.wait_for_error()

if __name__ == "__main__":
    run()
