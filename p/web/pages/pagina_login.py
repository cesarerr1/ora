from selenium.webdriver.common.by import By

class PaginaLogin:
    usuario_input = (By.NAME, 'username')
    password_input = (By.NAME, 'password')
    login_btn = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


