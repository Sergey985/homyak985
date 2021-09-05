from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\DB\chromedriver')
driver.get("https://preview.masterbucks.com")


print("Opening the main  page")
driver.implicitly_wait(15)
AcceptCoocies = driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-0']/app-show-popup/div/div[3]/button/span").click()
RegistrationButton = driver.find_element_by_css_selector(".wide-orange-button").click()
print("go to Sign In")

try:
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "kc-login"))
    )
finally:
    if not "Sign in to Identity" in driver.title:
       raise Exception("Unable to load MB Wallet page!")
    else:
       print("Page Sign In displayed")
usernamelogin = driver.find_element_by_id("username").send_keys("zbartenek@gmail.com")
passwordlogin = driver.find_element_by_id("password").send_keys("Sistema321")
buttonlogin = driver.find_element_by_id("kc-login").click()

try:
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "cdk-describedby-message-container"))
    )
finally:
    if driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").is_displayed():
       print("Page Wallet displayed")
    else:
       raise Exception("Unable load page Wallet")
