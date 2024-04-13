import pytest
import time
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get("https://www.quantman.in/")
        print(self.driver.title)
        login = "FT000000"
        pswd = "Password@123"
        dob = '01011901'
        
        self.driver.get("https://www.quantman.in/users/sign_in?locale=en")
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.ID, "dropdownMenuButton"))).click()
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//div[@value='flattrade']"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login with broker']"))).click()
        
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH,"//input[@id='flattrade-client-id']"))).send_keys(
            login)
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='btn-flattrade']"))).click()
        time.sleep(5)
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='input-17']"))).send_keys(login)
        time.sleep(2)
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='pwd']"))).send_keys(pswd)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='pan']"))).send_keys(dob)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Login')]"))).click()
        time.sleep(2)
        try:
            print("ap1")
            WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//i[contains(text(),'account_circle')]"))).click()
            print("cp1")
            ap = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//body/div[1]/nav[1]/div[1]/ul[1]/li[4]/div[1]/div[1]/span[2]")))
            print("cp2")
            ap = ap.text
            base_url = "BOTAPI:- DoneFlatrade " + ap[17:25]
        except:
            base_url = "BOTAPI" + login
        requests.get(base_url)
    
