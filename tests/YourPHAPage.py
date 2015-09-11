import os
from appium import webdriver
from time import sleep

locators = {
  'topmost_service' : '//UIAApplication[1]/UIAWindow[1]/UIATableView[2]/UIATableCell[1]/UIAButton[1]',
  'lets_go' : 'ActionButton',
  'messaging_tutorial' : 'Tell us how we can help you by sending a message to a Personal Health Assistant.',
  'topmost_service_message' : 'I want to get started reviewing my insurance coverage!',
  'close_service_overlay' : 'dismiss icn',
}

class YourPHAPage(object):

  def __init__(self,driver):
    self.driver = driver

  def select_service(self):
    self.driver.find_element_by_xpath(locators['topmost_service']).click()
    self.driver.find_element_by_name(locators['lets_go']).click()

  def select_only_service(self):
    self.driver.find_element_by_name(locators['lets_go']).click()

  def is_messaging_tutorial_present(self):
    list = self.driver.find_elements_by_name(locators['messaging_tutorial'])
    return len(list) > 0

  def is_selected_service_message_present(self):
    list = self.driver.find_elements_by_name(locators['topmost_service_message'])
    return len(list) > 0

  def decline_service(self):
    self.driver.find_element_by_name(locators['close_service_overlay']).click()
