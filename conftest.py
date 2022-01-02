import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="class")
def setup_fricture():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get('https://www.amazon.in/')
    # self.driver.maximize_window()
    driver.find_element_by_id('nav-link-accountList-nav-line-1').click()
    driver.find_element(By.XPATH, '//*[@id="ap_email"]').send_keys('917026121021')
    driver.find_element_by_id('continue').click()
    driver.find_element(By.XPATH, '//*[@id="ap_password"]').send_keys('yokshi3@')
    driver.find_element_by_id('signInSubmit').click()
    yield driver
    driver.quit()
