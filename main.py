from selenium import webdriver
import random as rd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\DB\chromedriver')
driver.get("")
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
usernamelogin = driver.find_element_by_id("username").send_keys("")
passwordlogin = driver.find_element_by_id("password").send_keys("")
buttonlogin = driver.find_element_by_id("kc-login").click()

try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "cdk-describedby-message-container"))
)
finally:
    print("Page Wallet displayed")

USD = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]")
print(USD.text + "Current USD balance")
AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
try:
     element = WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.ID, "mat-input-5")))
finally:
   print("form for adding amount displayed")

PaymentValue = rd.randint(1,9999)

AddFundsValue = driver.find_element_by_id("mat-input-5").send_keys(PaymentValue)
BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
print("Amount added. Selected option Credit Card")

if not driver.find_element_by_css_selector(".image-button img").is_enabled():
    raise Exception("Unable to load MB Wallet page!")
else:
    print("Button Credit Card is enabled")

BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
driver.implicitly_wait(5)
try:
     element = WebDriverWait(driver, 5).until(
     EC.presence_of_element_located((By.XPATH, "//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button"))
 )
finally:

   if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_displayed():
       raise Exception("Page Credit card list is not displayed")
   else:
       print("Credit card displayed")
driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/app-auth-net-mini-list/div/div/app-auth-net-mini/div/span").click()
print("Card selected")

if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_enabled():
    raise Exception("Payment impossible!")
else:
    print("Payment button enabled")

driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").click()

if not driver.find_element_by_css_selector(".status-text").is_displayed():
    raise Exception("Something wrong with payment")
else:
    print("Payment operation status: Success")

driver.find_element_by_css_selector(".orange-button > .mat-button-wrapper").click()

z = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]")
if z == USD + PaymentValue:
    print("Successfull payment. Value are equal to expected")


 # "mat-button-wrapper"  --- expand users items
    #driver.quit()