import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

locators = {
  'referral_code' : '//UIATextField',
  'referral_code_warning' : 'Referral code is invalid',
  'next' : 'ActionButton',
}

class EnterReferralCodePage(object):

  def __init__(self,driver):
    self.driver = driver

  def enter_referral_code(self,referral_code=''):

    self.driver.find_element_by_xpath(locators['referral_code']).send_keys(referral_code)
    self.driver.find_element_by_name(locators['next']).click()

  def is_referral_code_invalid_warning_present(self):
    list = self.driver.find_elements_by_name(locators['referral_code_warning'])
    return len(list) == 1 
