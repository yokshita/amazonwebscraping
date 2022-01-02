import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.sanity
@pytest.mark.tc_5
def test_cases5(setup_fricture):
    driver = setup_fricture
    #select amazon pay balance and choosing mobile recharge 5th testcase
    driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[3]  ').click()
    driver.find_element(By.XPATH, '//*[@id="MobileRecharge"]/span/a/div[1]/img  ').click()
    time.sleep(5)

@pytest.mark.sanity
@pytest.mark.tc_5
def test_cases5(setup_fricture):
    driver = setup_fricture
    # selecting witch country by using flags
    driver.find_element(By.XPATH, '//*[@id="icp-nav-flyout"]/span/span[2]/span[1]').click()
