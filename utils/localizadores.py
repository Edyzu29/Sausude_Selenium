from selenium.webdriver.common.by import By

#Login page
username_field = (By.CSS_SELECTOR,'#user-name')
password_field = (By.CSS_SELECTOR,'#password')
button_field = (By.CSS_SELECTOR,'#login-button')

examp_usaername_field = (By.XPATH, "//div[@id='login_credentials']//br")
examp_password_field = (By.CSS_SELECTOR, '.login_password')
#examp_password_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]/text()')

error_msg_field = (By.CSS_SELECTOR, '.error-message-container.error')