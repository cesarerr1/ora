from selenium.webdriver.common.by import By

class DatosContacto:

    xpath_address = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[{}]/div/div[2]/input'
    street_1_input = (By.XPATH, xpath_address.format(1))
    city_input = (By.XPATH, xpath_address.format(2))
    state_input = (By.XPATH, xpath_address.format(3))
    pc_input = (By.XPATH, xpath_address.format(4))

    xpath_country = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
    country_input = (By.XPATH, xpath_country)
    country_list = (By.XPATH, xpath_country + '[2]/div[*]/span')

    xpath_telephone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[{}]/div/div[2]/input'
    tel_home_input = (By.XPATH, xpath_telephone.format(1))
    tel_mobil_input = (By.XPATH, xpath_telephone.format(2))
    tel_work_input = (By.XPATH, xpath_telephone.format(3))

    xpath_email = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    work_email_input = (By.XPATH, xpath_email)

    save_button = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')

    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')

