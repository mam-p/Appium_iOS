import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

locators = {
  'first_name' : '//UIATextField',
  'birthdate' : 'Birthdate',
  'next' : 'ActionButton',
}

class CreateProfilePage(object):

  def __init__(self,driver):
    self.driver = driver

  def enter_profile_info(self,first_name="Appium"):

    self.driver.find_element_by_xpath(locators['first_name']).send_keys(first_name)
    self.driver.find_element_by_name(locators['birthdate']).click()
    self.driver.find_element_by_name(locators['next']).click()

  def is_action_button_enabled(self):
    return self.driver.find_element_by_name(locators['next']).is_enabled()

