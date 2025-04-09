from selenium.webdriver.common.by import By


class DatosPersonales:

    first_name_input = (By.NAME, 'firstName')
    middle_name_input = (By.NAME, 'middleName')
    last_name_input = (By.NAME, 'lastName')

    xpath_personal_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/'

    employee_id_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[1]/div[1]/div/div[2]/input')

    other_id_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[1]/div[2]/div/div[2]/input')
    driver_license_number_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[2]/div[1]/div/div[2]/input')
    license_expiry_date = (
        By.XPATH, xpath_personal_details + 'div[2]/div[2]/div[2]/div/div[2]/div/div/input')

    nationality = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[1]/div/div[2]/div/div[1]')
    nationality_list = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[*]/span')

    marital_status = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[2]/div/div[2]/div/div[1]')
    marital_status_list = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[*]/span')

    birth_date = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[1]/div/div[2]/div/div/input')
    gender_male_radio = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div')
    gender_female_radio = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div')

    save_personal_details_button = (
        By.XPATH, xpath_personal_details + 'div[4]/button')

    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')

    error_message = (By.XPATH,".//span[contains(@class, 'oxd-input-field-error-message')]")

