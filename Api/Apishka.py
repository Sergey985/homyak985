import datetime
import time
import requests
import json

def dnp_dev_calculate():
    url = ""

    payload = json.dumps({
        "domain_name": "synalov.cz",
        'priority': '63'

    })
    headers = {
        'Content-Type': 'application/json'

    }
    i = 0
    response = requests.request("POST", url, headers=headers, data=payload)
    t = datetime.datetime.now()
    print("Start time:" + " " + str(t))
    print(response.text)
    print(response.status_code)
    while response.json()['status_value']!=2:
          response = requests.request("POST", url, headers=headers, data=payload)
          i=i+1
          t1 = datetime.datetime.now()
          t2 = t1 - t
          print(str(t2) + " " + str(i) + " " + "Due operation. Recent status is:" + " " + str(response.json()['status_value']))
    else:
        print("recalculated")

def dnp_dev_details():
    url = ""
    payload = json.dumps({
      "domain_name": "synalov.cz"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)
    #print(response.json()['marks'][0]['registered'])