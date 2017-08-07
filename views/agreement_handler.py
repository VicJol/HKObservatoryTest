from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class AgreementHandler():
    agree_button_xpath = "//android.widget.Button[@text='Agree']"
    update_version_cross_button_xpath = "//android.widget.ImageButton"
    main_page_title_xpath = "//android.widget.TextView[@text='MyObservatory']"

    def __init__(self ,driver):
        self.driver = driver

    def handle_agreement(self):
        """
        If agreement page shows up, click "Agree" buttons and wait to load the main page        
        """
        agree_button = self.driver.find_element_by_xpath(self.agree_button_xpath)

        if agree_button.is_displayed():
            agree_button.click()
            agree_button.click()
            allow_button = self.driver.find_element_by_class_name("android.widget.Button")
            allow_button.click()
        else:
            try:
                WebDriverWait(self.driver,30).until(EC.presence_of_element_located(By.XPATH, self.main_page_title_xpath))
                self.driver.find_element_by_xpath(self.main_page_title_xpath)
            except:
                logging.warning('Main page is not loaded.')

    def handle_update_version(self):
        """
        If the update version page shows up, close it and wait to load main page
        """
        update_version_cross_button = self.driver.find_element_by_xpath(self.update_version_cross_button_xpath)
        update_version_cross_button_by = (By.XPATH,self.update_version_cross_button_xpath)

        if update_version_cross_button.is_displayed():
            try:
                WebDriverWait(self.driver,30).until(EC.presence_of_element_located(update_version_cross_button_by))
                update_version_cross_button.click()
            except Exception as e:
                logging.error(e)
