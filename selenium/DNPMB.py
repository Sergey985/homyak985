from selenium import webdriver
import re
import random as rd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread, Barrier
def func(DNPMB):
    driver = webdriver.Chrome(r'C:\DB\chromedriver')
    driver.get(url)

    # print("Opening the main  page")
    # driver.implicitly_wait(15)
    #
    # print("go to Sign In")
    #
    # try:
    #     element = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, "//input[@id='mat-input-1']"))
    # )
    # finally:
    #     if not "Purchase a warranty for a domain - DNProtect" in driver.title:
    #         raise Exception("Unable to load domain protection page!")
    #     else:
    #         print("Page protect domain displayed")
    # BusinessName = driver.find_element_by_xpath("//input[@id='mat-input-1']").send_keys("Bartek")
    # AnnualRevenue = driver.find_element_by_xpath("//input[@id='mat-input-2']").send_keys("12")
    # YearofFounding = driver.find_element_by_xpath("//input[@id='mat-input-3']").send_keys("2020")
    # NumbEmpl = driver.find_element_by_xpath("//input[@id='mat-input-4']").send_keys("2")
    # ExpandListofIndustry = driver.find_element_by_xpath("//mat-select[@id='mat-select-0']/div/div[2]/div").click()
    # SelectItemDropDown = driver.find_element_by_xpath("//span[contains(.,'Accounting')]").click()
    # BUttonNext = driver.find_element_by_xpath("//button[contains(.,'Next')]").click()
    # SecondButtonNext = driver.find_element_by_xpath("//div[@id='cdk-step-content-0-1']/form/div[5]/button[2]").click()
    # ThirdButtonNext = driver.find_element_by_xpath("//div[@id='cdk-step-content-0-2']/form/div[4]/button[2]").click()
    #
    # try:
    #     element = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[@id='cdk-step-content-0-3']/form/div[2]/mat-form-field/div/div/div/input"))
    # )
    # finally:
    #     if not driver.find_element_by_xpath("//div[@id='cdk-step-content-0-3']/form/div[2]/mat-form-field/div/div/div/input"):
    #         raise Exception("Unable to load domain protection page!")
    #     else:
    #         print("Page Your contact information is displayed")
    #
    # driver.find_element_by_xpath("//div[@id='cdk-step-content-0-3']/form/div[2]/mat-form-field/div/div/div/input").send_keys("Bartek")
    # driver.find_element_by_xpath("//div[@id='cdk-step-content-0-3']/form/div[2]/mat-form-field[2]/div/div/div/input").send_keys("zbartenek@gmail.com")
    # driver.find_element_by_xpath("//input[@id='mat-input-16']").send_keys("22332122122")
    # driver.find_element_by_xpath("//input[@id='mat-input-17']").send_keys("2233212212")
    # driver.find_element_by_xpath("//input[@id='mat-input-18']").send_keys("2233212212")
    # driver.find_element_by_xpath("//input[@id='mat-input-19']").send_keys("2233212212")
    # driver.find_element_by_xpath("//input[@id='mat-input-20']").send_keys("2233212212")
    # driver.find_element_by_xpath("//input[@id='mat-input-21']").send_keys("2233212212")
    # driver.find_element_by_xpath("//input[@id='mat-input-22']").send_keys("223321")
    # driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-8']/label/span").click()
    # driver.find_element_by_xpath("//mat-checkbox[@id='mat-checkbox-9']/label/span").click()
    # if not driver.find_element_by_xpath("//div[@id='cdk-step-content-0-3']/form/div[7]/button[2]"):
    #     raise Exception("Button Purchase disabled")
    # else:
    #     print("Checked: button Purchase enabled")
    #     driver.find_element_by_xpath("//div[@id='cdk-step-content-0-3']/form/div[7]/button[2]").click()
    # driver.find_element_by_xpath("//mat-dialog-container[@id='mat-dialog-0']/whq-confirmation-dialog/mat-dialog-actions/button[2]/span").click()
    #
    # print("go to Sign In")
    #
    # try:
    #     element = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.ID, "kc-login"))
    # )
    # finally:
    #     if not "Sign in to Identity" in driver.title:
    #         raise Exception("Unable to load MB Wallet page!")
    #     else:
    #         print("Page Sign In displayed")
    # usernamelogin = driver.find_element_by_id("username").send_keys("")
    # passwordlogin = driver.find_element_by_id("password").send_keys("")
    # buttonlogin = driver.find_element_by_id("kc-login").click()
    #
    # try:
    #     element = WebDriverWait(driver, 75).until(
    #     EC.presence_of_element_located((By.XPATH, "//div[3]/button/span"))
    # )
    # finally:
    #     if not driver.find_element_by_xpath("//div[3]/button/span"):
    #         raise Exception("Unable to load MB payment page!")
    #     else:
    #         print("Page MB payment displayed")
    # driver.implicitly_wait(200)
    AcceptCoocies = driver.find_element_by_css_selector("path:nth-child(2)").click()
    MBPayment = driver.find_element_by_xpath("//mat-radio-button[@id='mat-radio-2']/label/span[2]").click()
    Payment = driver.find_element_by_xpath("//div[2]/div/button").click()
    print("Payment's done")
    OkAccept= driver.find_element_by_css_selector(".orange-button").click()
    if driver.find_element_by_xpath("//div[2]/button"):
        print("payment added succesfully")
    else:
        print("test failed")
url = ("")
number_of_threads = 2
DNPMB = Barrier(number_of_threads)
threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(DNPMB,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()
#driver.quit()