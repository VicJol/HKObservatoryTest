import unittest
from appium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # create a session
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '5.4  FWVGA API 25'
        desired_caps['appPackage'] = 'hko.MyObservatory_v1_0'
        desired_caps['appActivity'] = '.AgreementPage'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()