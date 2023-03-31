# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLockedOutUser():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lockedOutUser(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1382, 744)
    WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable((By.ID, "password")))
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    self.driver.find_element(By.ID, "login-button").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Sorry, this user has been locked out."
  
