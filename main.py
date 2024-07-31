from case_test import *



def run():
    login_page_test_sauce = Cases_test()
    login_page_test_sauce.setup_class()
    login_page_test_sauce.collect_credencials()

if __name__ == "__main__":
    run()
