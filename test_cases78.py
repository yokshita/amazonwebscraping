import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.regression
@pytest.mark.tc_7
def test_cases7(setup_fricture):
    driver = setup_fricture
    # open kindle ebooks and check deals on kindle ebooks
    driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[4]').click()
    driver.find_element(By.XPATH, '//*[@id="nav-subnav"]/a[6]/span').click()
    time.sleep(3)


@pytest.mark.regression
@pytest.mark.tc_8
def test_cases8(setup_fricture):
    driver = setup_fricture
    #open all tab and select fire tv and opens primevedio
    driver.find_element(By.XPATH, '//*[@id="nav-hamburger-menu"]/span').click()
    driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[8]/a').click()
    driver.find_element(By.XPATH, '//*[@id="hmenu-content"]/ul[3]/li[7]/a').click()
    time.sleep(3)


