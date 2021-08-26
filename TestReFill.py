from selenium import webdriver
import re
import random as rd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\DB\chromedriver')
driver.get("https://masterbucks.com/")
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
passwordlogin = driver.find_element_by_id("password").send_keys("Sistem32")
buttonlogin = driver.find_element_by_id("kc-login").click()

try:
    element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "cdk-describedby-message-container"))
)
finally:
    print("Page Wallet displayed")
#
# USD = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
# USD = USD.replace(' ','')
# USD = USD.replace(',','.')
# USD = float(USD)
# print("Recent balance:")
# print(USD)
#
# AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
# try:
#      element = WebDriverWait(driver, 15).until(
#      EC.presence_of_element_located((By.ID, "mat-input-5")))
# finally:
#    print("form for adding amount displayed")
#
# PaymentValue = rd.randint(1,9999)
#
# AddFundsValue = driver.find_element_by_id("mat-input-5").send_keys(PaymentValue)
# print("Payment:")
# print(PaymentValue)
# BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
# print("Amount added. Selected option Credit Card")
#
# if not driver.find_element_by_css_selector(".image-button img").is_enabled():
#     raise Exception("Unable to load MB Wallet page!")
# else:
#     print("Button Credit Card is enabled")
#
# BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
# driver.implicitly_wait(5)
# try:
#      element = WebDriverWait(driver, 15).until(
#      EC.presence_of_element_located((By.XPATH, "//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button"))
#  )
# finally:
#
#    if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_displayed():
#        raise Exception("Page Credit card list is not displayed")
#    else:
#        print("Credit card displayed")
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/app-auth-net-mini-list/div/div/app-auth-net-mini/div/span").click()
# print("Card selected")
#
# if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_enabled():
#     raise Exception("Payment impossible!")
# else:
#     print("Payment button enabled")
#
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").click()
#
# if not driver.find_element_by_css_selector(".status-text").is_displayed():
#     raise Exception("Something wrong with payment")
# else:
#     print("Payment operation status: Success")
#
# driver.find_element_by_css_selector(".orange-button > .mat-button-wrapper").click()
#
# z = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
# z = z.replace(' ','')
# z = z.replace(',','.')
#
# z = USD + PaymentValue
# if z != USD + PaymentValue:
#
#     print("Recent balance:")
#     print(USD)
#     print("Payment value:")
#     print(PaymentValue)
#     print("Resultative balance:")
#     print(z)
#     raise Exception("Value aren't equal")
# else:
#     print("Successfull payment. Value are equal to expected")
#
#    Check USD Gift refill

# driver.find_element_by_xpath("//div[@id='GFD']/div/span[2]").click()
# USDgift = driver.find_element_by_xpath("//div[@id='GFD']/div/span[2]").text
# USDgift = USDgift.replace(' ','')
# USDgift = USDgift.replace(',','.')
# USDgift = float(USDgift)
# print("Recent balance:")
# print(USDgift)
#
# AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
# try:
#      element = WebDriverWait(driver, 10).until(
#      EC.presence_of_element_located((By.ID, "mat-input-10")))
# finally:
#    print("form for adding amount displayed")
#
# PaymentValue = rd.randint(1,999)
#
# AddFundsValue = driver.find_element_by_id("mat-input-10").send_keys(PaymentValue)
# print("Payment:")
# print(PaymentValue)
# BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
# print("Amount added. Selected option Credit Card")
#
# if not driver.find_element_by_css_selector(".image-button img").is_enabled():
#     raise Exception("Unable to load MB Wallet page!")
# else:
#     print("Button Credit Card is enabled")
#
# BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
# driver.implicitly_wait(5)
# try:
#      element = WebDriverWait(driver, 15).until(
#      EC.presence_of_element_located((By.XPATH, "//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button"))
#  )
# finally:
#
#    if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_displayed():
#        raise Exception("Page Credit card list is not displayed")
#    else:
#        print("Credit card displayed")
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/app-auth-net-mini-list/div/div/app-auth-net-mini/div/span").click()
# print("Card selected")
#
# if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_enabled():
#     raise Exception("Payment impossible!")
# else:
#     print("Payment button enabled")
#
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").click()
#
# if not driver.find_element_by_css_selector(".status-text").is_displayed():
#     raise Exception("Something wrong with payment")
# else:
#     print("Payment operation status: Success")
#
# driver.find_element_by_css_selector(".orange-button > .mat-button-wrapper").click()
#
# z1 = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
# z1 = z1.replace(' ','')
# z1 = z1.replace(',','.')
#
# z1 = USDgift + PaymentValue
# if z1 != USDgift + PaymentValue:
#
#     print("Recent balance:")
#     print(USDgift)
#     print("Payment value:")
#     print(PaymentValue)
#     print("Resultative balance:")
#     print(z1)
#     raise Exception("Value aren't equal")
# else:
#     print("Successfull payment. Value are equal to expected")
#

#    Check EUR refill
#
# driver.find_element_by_xpath("//div[@id='EUR']/div/span[2]").click()
# EUR = driver.find_element_by_xpath("//div[@id='EUR']/div/span[2]").text
# EUR = EUR.replace(' ','')
# EUR = EUR.replace(',','.')
# EUR = float(EUR)
# print("Recent balance:")
# print(EUR)
#
# AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
# try:
#      element = WebDriverWait(driver, 10).until(
#      EC.presence_of_element_located((By.ID, "mat-input-10")))
# finally:
#    print("form for adding amount displayed")
#
# PaymentValue = rd.randint(1,9999)
#
# AddFundsValue = driver.find_element_by_id("mat-input-10").send_keys(PaymentValue)
# print("Payment:")
# print(PaymentValue)
# BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
# print("Amount added. Selected option Credit Card")
#
# if not driver.find_element_by_css_selector(".image-button img").is_enabled():
#     raise Exception("Unable to load MB Wallet page!")
# else:
#     print("Button Credit Card is enabled")
#
# BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
# driver.implicitly_wait(5)
# try:
#      element = WebDriverWait(driver, 15).until(
#      EC.presence_of_element_located((By.XPATH, "//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button"))
#  )
# finally:
#
#    if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_displayed():
#        raise Exception("Page Credit card list is not displayed")
#    else:
#        print("Credit card displayed")
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/app-auth-net-mini-list/div/div/app-auth-net-mini/div/span").click()
# print("Card selected")
#
# if not driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").is_enabled():
#     raise Exception("Payment impossible!")
# else:
#     print("Payment button enabled")
#
# driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-1']/app-auth-net-pay/div[2]/div/div/button").click()
#
# if not driver.find_element_by_css_selector(".status-text").is_displayed():
#     raise Exception("Something wrong with payment")
# else:
#     print("Payment operation status: Success")
#
# driver.find_element_by_css_selector(".orange-button > .mat-button-wrapper").click()
#
# z2 = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
# z2 = z2.replace(' ','')
# z2 = z2.replace(',','.')
#
# z2 = EUR + PaymentValue
# if z2 != EUR + PaymentValue:
#
#     print("Recent balance:")
#     print(EUR)
#     print("Payment value:")
#     print(PaymentValue)
#     print("Resultative balance:")
#     print(z2)
#     raise Exception("Value aren't equal")
# else:
#     print("Successfull payment. Value are equal to expected")

# #    Check CAD refill
for i in range(4):
    driver.find_element_by_xpath("//div[2]/div[3]/div").click()
driver.find_element_by_xpath("//div[@id='CAD']/div").click()
CAD = driver.find_element_by_xpath("//div[@id='CAD']/div").text
CAD = CAD.replace(' ','')
CAD = CAD.replace(',','.')
CAD = re.sub('\D', '', CAD)
CAD = float(CAD)
print("Recent balance:")
print(CAD)

AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
try:
     element = WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.ID, "mat-input-10")))
finally:
   print("form for adding amount displayed")

PaymentValue = rd.randint(1,9999)

AddFundsValue = driver.find_element_by_id("mat-input-10").send_keys(PaymentValue)
print("Payment:")
print(PaymentValue)
BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
print("Amount added. Selected option Credit Card")

if not driver.find_element_by_css_selector(".image-button img").is_enabled():
    raise Exception("Unable to load MB Wallet page!")
else:
    print("Button Credit Card is enabled")

BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
driver.implicitly_wait(5)
try:
     element = WebDriverWait(driver, 15).until(
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

z3 = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
z3 = z3.replace(' ','')
z3 = z3.replace(',','.')

z3 = CAD + PaymentValue
if z3 != CAD + PaymentValue:

    print("Recent balance:")
    print(CAD)
    print("Payment value:")
    print(PaymentValue)
    print("Resultative balance:")
    print(z3)
    raise Exception("Value aren't equal")
else:
    print("Successfull payment. Value are equal to expected")

 #  Check GBP refill

driver.find_element_by_xpath("//div[2]/div[3]/div").click()
driver.find_element_by_xpath("//div[@id='GBP']/div").click()
GBP = driver.find_element_by_xpath("//div[@id='GBP']/div").text
GBP = GBP.replace(' ','')
GBP = GBP.replace(',','.')
GBP = re.sub('\D', '', GBP)
GBP = float(GBP)
print("Recent balance:")
print(GBP)

AddFunds = driver.find_element_by_xpath("//div/div/button/span/span").click()
try:
     element = WebDriverWait(driver, 20).until(
     EC.presence_of_element_located((By.ID, "mat-input-16")))
finally:
   print("form for adding amount displayed")

PaymentValue = rd.randint(1,99)

AddFundsValue = driver.find_element_by_id("mat-input-16").send_keys(PaymentValue)
print("Payment:")
print(PaymentValue)
BUttonCC = driver.find_element_by_xpath("//app-template-radio-item[2]/mat-radio-button/label/span").click()
print("Amount added. Selected option Credit Card")

if not driver.find_element_by_css_selector(".image-button img").is_enabled():
    raise Exception("Unable to load MB Wallet page!")
else:
    print("Button Credit Card is enabled")

BUttonAuthorizeNet = driver.find_element_by_css_selector(".image-button img").click()
driver.implicitly_wait(10)
try:
     element = WebDriverWait(driver, 15).until(
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

z4 = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
z4 = z4.replace(' ','')
z4 = z4.replace(',','.')

z4 = GBP + PaymentValue
if z4 != GBP + PaymentValue:

    print("Recent balance:")
    print(GBP)
    print("Payment value:")
    print(PaymentValue)
    print("Resultative balance:")
    print(z4)
    raise Exception("Value aren't equal")
else:
    print("Successfull payment. Value are equal to expected")
 # "mat-button-wrapper"  --- expand users items
    #driver.quit()