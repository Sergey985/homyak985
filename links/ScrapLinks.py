from bs4 import BeautifulSoup as bs
import math
import requests
import BD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import Column, Integer, Table, String, create_engine, ForeignKey, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased, Query
import unittest, time

engine = create_engine('sqlite:///C:/DB/test.db', echo=True)

driver = webdriver.Chrome(r'C://DB//chromedriver')
driver.implicitly_wait(10)

branch = ["", ""]
# branch.__str__()
tt=0
ttt=0
while tt < 10:

    for i in branch:
        url = i

    # html = requests.get(url)
        soup = bs(requests.get(url).content, "html.parser")
        current_link = ''

        for link in soup.find_all('a'):
            current_link = link.attrs.get('href')
            print(current_link)
            if current_link in {
            "",
            None,
            "/",
            "",
            "",
        }:

                continue
        # driver.refresh()
            _start = time.perf_counter_ns()
            driver.get(f"{url}{current_link}")
            _stop = time.perf_counter_ns()
            print(f"{current_link}: {(_stop - _start)/(10**6)}")
            stext =(_stop - _start)/(10**6)
            test = int(stext)


            print(current_link + " " + "Value is: %s" % stext)
            ins = BD.syu.insert().values(Branch=url, URLLinks=current_link, Time=stext)
            con = engine.connect()
            result = con.execute(ins)
            ttt=ttt+1
            print(ttt)
driver.quit()
