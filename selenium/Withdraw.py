from selenium import webdriver
import re
import random as rd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from threading import Thread, Barrier


def func(withdraw):
    driver = webdriver.Chrome(r'C:\DB\chromedriver')
    driver.get(url)
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
    usernamelogin = driver.find_element_by_id("username").send_keys("")
    passwordlogin = driver.find_element_by_id("password").send_keys("")
    buttonlogin = driver.find_element_by_id("kc-login").click()

    USD = driver.find_element_by_xpath("//div[@id='USD']/div/span[2]").text
    USD = USD.replace(' ', '')
    USD = USD.replace(',', '.')
    USD = float(USD)

    Withdraw = driver.find_element_by_xpath("//button[2]/span/span").click()
    SelectPayment = driver.find_element_by_css_selector("#mat-radio-6 .mat-radio-label-content").click()
    ButtonContinue = driver.find_element_by_xpath("//div[2]/div/div/div[2]/button/span").click()
    Input = driver.find_element_by_xpath("//input[@id='mat-input-5']").send_keys(2)
    WithdrawButton = driver.find_element_by_xpath("//div[3]/div[2]/button[2]").click()
    Done = driver.find_element_by_xpath("//div[3]/div/div/div[2]/button").click()

url = ''
number_of_threads = 2
withdraw = Barrier(number_of_threads)
threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(withdraw,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

# Input2fa = driver.find_element_by_xpath("//input[@id='mat-input-19']").send_keys(num)
# Accept = driver.find_element_by_xpath("//app-form-2fa/div/div[2]/button[2]").click()
