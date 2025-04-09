from selenium.webdriver.common.by import By


class MenuMiInformacion:
    xpath_menu = "//a[contains(@class, 'orangehrm-tabs-item') and contains(text(), '{}')]"

    personal_details_button = (By.XPATH, xpath_menu.format("Personal Details"))
    contact_details_button = (By.XPATH, xpath_menu.format("Contact Details"))
    emergency_contacts_button = (By.XPATH, xpath_menu.format("Emergency Contacts"))
    dependents_button = (By.XPATH, xpath_menu.format("Dependents"))
    immigration_button = (By.XPATH, xpath_menu.format("Inmigration"))
    job_button = (By.XPATH, xpath_menu.format("Job"))
    salary_button = (By.XPATH, xpath_menu.format("Salary"))
    report_to_button = (By.XPATH, xpath_menu.format("Report-to"))
    qualifications_button = (By.XPATH, xpath_menu.format("Qualifications"))
    memberships_button = (By.XPATH, xpath_menu.format("Memberships"))

