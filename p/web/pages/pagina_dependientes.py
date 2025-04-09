from selenium.webdriver.common.by import By


class Dependientes:
    xpath_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]'

    add_dependent_button = (By.XPATH, xpath_dependents + '/div/button')
    save_dependent_button =(By.XPATH, xpath_dependents + '/form/div[3]/button[2]')

    name_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[1]/div/div[2]/input')
    relationship_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
    relationship_list =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[*]/span')
    please_specify_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[3]/div/div[2]/input')
    date_birth_input =(By.XPATH, xpath_dependents + '/form/div[2]/div/div/div/div[2]/div/div/input')
    
    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')
