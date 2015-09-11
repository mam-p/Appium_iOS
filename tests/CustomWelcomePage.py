import os
from random import randint
from appium import webdriver
from time import sleep
from helpers import get_default_password, generate_email

locators = {
  'next' : 'ActionButton',
  'default_background' : 'FamilyBackground-Blurry.jpg'
}

class CustomWelcomePage(object):

  def __init__(self,driver):
    self.driver = driver

  def tap_next(self):
    self.driver.find_element_by_name(locators['next']).click()

#  def is_default_background_displayed(self):
#    list = self.driver.find_elements_by_name(locators['default_background'])
#    if (list[0]):
#      locator = list[0]
#      print "Inside PO if statement"
#      print locator.is_displayed()
#      return locator.is_displayed()
#    return false  # not findable === not displayed
# TODO Dan : Have the app quit loading the default image - Appium returns True for both of the two calls below
#    print self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAImage[1]').is_displayed()
#    print self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAImage[2]').is_displayed()
#    return self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAImage[1]').is_displayed()
