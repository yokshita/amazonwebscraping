import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.regression
@pytest.mark.tc_3
def test_cases3(setup_fricture):
    driver= setup_fricture
    # selecting fresh bar and choosing baby products 3rd testcase
    driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]').click()
    driver.find_element(By.XPATH, '//*[@id="nav-subnav"]/a[9]/span[1]').click()
    time.sleep(5)

@pytest.mark.regression
@pytest.mark.tc_4
def test_cases4(setup_fricture):
    driver = setup_fricture
    #by searching girls fashion and selecting Girls fashion and jumpsuits 4th testcase
    driver.find_element_by_name('field-keywords').send_keys('girls fashion')
    driver.find_element_by_id('nav-search-submit-button').click()
    driver.find_element(By.XPATH, '//*[@id="n/15966953031"]/div/span')
    time.sleep(5)
