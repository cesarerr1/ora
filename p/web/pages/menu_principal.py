from selenium.webdriver.common.by import By

class MenuPrincipal:
    xpath_menu = "//span[text()='{}' and contains(@class, 'oxd-main-menu-item--name')]"

    search_input = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div')
    admin_button = (By.XPATH, xpath_menu.format("Admin"))
    pim_button = (By.XPATH, xpath_menu.format("PIM"))
    leave_button = (By.XPATH, xpath_menu.format("Leave"))
    time_button = (By.XPATH, xpath_menu.format("Time"))
    recruitment_button = (By.XPATH, xpath_menu.format("Recruitment"))
    my_info_button = (By.XPATH, xpath_menu.format("My Info"))
    performance_button = (By.XPATH, xpath_menu.format("Performance"))
    dashboard_button = (By.XPATH, xpath_menu.format("Dashboard"))
    directory_button = (By.XPATH, xpath_menu.format("Directory"))
    maintenance_button = (By.XPATH, xpath_menu.format("Maintenance"))
    claim_button = (By.XPATH, xpath_menu.format("Claim"))
    buzz_button = (By.XPATH, xpath_menu.format("Buzz"))
