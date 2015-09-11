"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app='/Users/mam-p/Library/Developer/CoreSimulator/Devices/3DBA690A-A052-47FD-94AE-5DD623DA22E7/data/Containers/Bundle/Application/096EA798-2029-4D92-B8F7-8D805EBEE0E4/better-qa.app'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '8.3',
                'deviceName': 'iPhone 6'
            })
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_first(self):
        self.driver.find_element_by_name('ActionButton').click()

        email_address = generate_email()
        self.driver.find_element_by_xpath('//UIATextField').send_keys(email_address)
        self.driver.find_element_by_name('ActionButton').click()

        self.driver.find_element_by_name('tos unchecked').click()
        password = get_default_password()
        self.driver.find_element_by_xpath('//UIASecureTextField[1]').send_keys(password)
        self.driver.find_element_by_name('ActionButton').click()
 
        self.driver.find_element_by_xpath('//UIATextField').send_keys('Appium')
        self.driver.find_element_by_name('Birthdate').click()
        self.driver.find_element_by_name('Next').click()

        self.driver.find_element_by_xpath('//UIATextField').send_keys('group-many')
        self.driver.find_element_by_name('ActionButton').click()
        sleep(5)      # Simulate user who stops briefly to read welcome text message
        self.driver.find_element_by_name('ActionButton').click()

        self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAButton[1]').click()
        self.driver.find_element_by_name('ActionButton').click()

        online_status = self.driver.find_elements_by_name('ONLINE')
        offline_status = self.driver.find_elements_by_name('OFFLINE')

        assert len(online_status) + len(offline_status) == 1, "Neither ONLINE nor OFFLINE status displayed on Your PHA page"

        if (len(online_offline_status) > 0):
          print 'offline'
        else:
            print 'online'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=1).run(suite)
