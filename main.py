from selenium import webdriver
import random as rd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\DB\chromedriver')
driver.get("https://preview.masterbucks.com/")
print("Opened main  page")
driver.implicitly_wait(15)
AcceptCoocies = driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-0']/app-show-popup/div/div[3]/button/span").click()
RegistrationButton = driver.find_element_by_css_selector(".wide-orange-button").click()
print("go to Sign In")

try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "kc-login"))
)
finally:
    if not "Sign in to Identity" in driver.title:
        raise Exception("Unable to load MB Wallet page!")
print("Page Sign In displayed")
usernamelogin = driver.find_element_by_id("username").send_keys("zbartenek@gmail.com")
passwordlogin = driver.find_element_by_id("password").send_keys("Sistem32")
buttonlogin = driver.find_element_by_id("kc-login").click()

try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "cdk-describedby-message-container"))
)
finally:
    print("Page Wallet displayed")