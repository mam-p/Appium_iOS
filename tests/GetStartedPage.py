import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

class GetStartedPage(object):

  def __init__(self,driver):
    self.driver = driver

  locators = {
  }

  def tap_action_button(self):
    self.driver.find_element_by_name('ActionButton').click()
