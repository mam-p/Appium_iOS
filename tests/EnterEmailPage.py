import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

locators = {
  'email_address_field' : '//UIATextField',
  'next' : 'ActionButton',
}

class EnterEmailPage(object):

  def __init__(self,driver):
    self.driver = driver

  def tap_action_button(self):
    self.driver.find_element_by_name('ActionButton').click()

  def enter_email(self,email_address=generate_email()):
    self.driver.find_element_by_xpath(locators['email_address_field']).send_keys(email_address)
    self.driver.find_element_by_name(locators['next']).click()

  def is_action_button_enabled(self):
    return self.driver.find_element_by_name(locators['next']).is_enabled()
