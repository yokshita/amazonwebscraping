import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.smoke
@pytest.mark.tc_1
def test_open_url(setup_fricture):
    driver = setup_fricture
    #by searching samsung mobiles 1st test case
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys('samsung mobiles')
    driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]').click()
    time.sleep(5)


@pytest.mark.smoke
@pytest.mark.tc_2
def test_mensfashion(setup_fricture):
    driver = setup_fricture
    # by choosing all tab and select mens fashion and enter into sports shoes 2nd testcase
    driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[17]/a').click()
    driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[10]/li[18]/a').click()
    time.sleep(5)


