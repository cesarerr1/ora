from selenium.webdriver.common.by import By  # type: ignore


class Afiliaciones:
    def __init__(self):

        xpath_membership = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/'
        
        self.assigned_membership = (
            By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button')
        
        
        self.membership = (
            By.XPATH,xpath_membership +'div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]')
        
        self.membership_list = (
            By.XPATH, xpath_membership +'div[1]/div/div[1]/div/div[2]/div/div[2]/div[*]/span') 
        
        self.suscription = (
            By.XPATH, xpath_membership + 'div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        
        self.suscription_list = (
            By.XPATH, xpath_membership + 'div[1]/div/div[2]/div/div[2]/div/div[2]/div[*]/span')
        
        self.suscription_mount = (
            By.XPATH, xpath_membership + 'div[1]/div/div[3]/div/div[2]/input'
        )

        self.currency = (
            By.XPATH, xpath_membership + 'div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]'
        )

        self.currency_list = (
            By.XPATH, xpath_membership + 'div[1]/div/div[4]/div/div[2]/div/div[2]/div[*]/span'
        )

        self.date_suscription_start = (
            By.XPATH, xpath_membership + 'div[1]/div/div[5]/div/div[2]/div/div/input'
        )

        self.date_suscription_final = (
            By.XPATH, xpath_membership + 'div[1]/div/div[6]/div/div[2]/div/div/input'
        )

        self.save_btn_membership = (
            By.XPATH, xpath_membership + 'div[2]/button[2]'
        )

        self.add_file_membership = (
            
            By.CSS_SELECTOR,".oxd-file-input"
        )

        self.add_attachments_membership = (
            By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div[1]/div/button'
        )

        self.save_btn_file = (
            By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-attachment > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space"
        )

        self.delete_membership = (
            By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space' and i[@class='oxd-icon bi-trash']]"
        )

        self.confirmation_delete_membership = (
            By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]'
        )

        self.download_file = (
            By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space' and i[@class='oxd-icon bi-download']]"
        )

        self.error_message = (
            By.XPATH, ".//span[contains(@class, 'oxd-input-field-error-message')]"
        )

        



        

        
        
        

