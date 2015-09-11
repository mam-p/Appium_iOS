import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

locators = {
  'new_password' : '//UIASecureTextField[1]',
  'tos' : 'tos unchecked',
  'next' : 'ActionButton',
}

class CreatePasswordPage(object):

  def __init__(self,driver):
    self.driver = driver

  def enter_new_password(self,password=get_default_password()):
    password_locator = self.driver.find_element_by_xpath(locators['new_password'])
    password_locator.click()
    password_locator.send_keys(password)
    self.driver.find_element_by_name(locators['tos']).click()
    self.driver.find_element_by_name(locators['next']).click()

  def is_action_button_enabled(self):
    return self.driver.find_element_by_name('ActionButton').is_enabled()
