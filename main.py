from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from numpy import random
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

df = pd.read_excel(os.environ.get('DOCUMENT_PATH'))
email = df.iloc[0,4]
phone = "{}".format(df.iloc[0,5])[3:12]


## open chrome
browser = wd.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)

## open alza.cz
browser.get("https://www.alza.cz/EN/")

# Accept cookies
time.sleep(random.randint(6, 10))
browser.find_element(By.XPATH, '//*[@id="rootHtml"]/body/div[7]/div/div/div[2]/a[1]').click() 


for x in range(len(df)):
    product_code = df.iloc[x,1]
        
    ## Shopping process
    # Add products
    time.sleep(random.randint(3, 6))
    search_button = browser.find_element(By.XPATH, '//*[@id="edtSearch"]') # find search section
    search_button.send_keys(product_code + Keys.ENTER) # Insert product code and press enter

    time.sleep(random.randint(6, 8)) # wait a few seconds
    browser.find_element(By.XPATH, '//*[@id="boxes"]/div[1]/div[2]/div[1]/span/div/div/a').click() # buy button, add to cart

    try:
        time.sleep(random.randint(3, 5)) # wait a few seconds
        browser.find_element(By.XPATH, '//*[@id="alzaDialog"]/div[3]/div/div[3]/span[2]').click() # pop up window add to cart
    except:
        pass

    try:
        time.sleep(random.randint(5, 8)) # wait a few seconds
        browser.find_element(By.XPATH, '//*[@id="varBToBasketButton"]/span').click() # proceed to checkout
    except:
        time.sleep(1) # wait a few seconds
        browser.find_element(By.XPATH, '//*[@id="basketLink"]').click() # go to basket

    time.sleep(random.randint(6, 8))
    browser.find_element(By.XPATH, '//*[@id="blockBtnRight"]/a/span[1]').click() # continue

    try:
        time.sleep(random.randint(4, 6))
        browser.find_element(By.XPATH, '//*[@id="alzaDialog"]/div[3]/div[2]/span[1]').click() # do not add anything
    except:
        pass

    time.sleep(random.randint(5, 8))
    elem = browser.find_element(By.XPATH, '//*[@id="deliveryCheckbox-595"]') # select delivery method
    browser.execute_script("arguments[0].click();", elem)

    time.sleep(random.randint(4, 8))
    browser.find_element(By.XPATH, '//*[@id="personalCentralDialog"]/div[2]/a[2]').click() # confirm selection

    time.sleep(random.randint(4, 8))
    browser.find_element(By.XPATH, '//*[@id="showAllPayments"]/i').click() # all payment options

    time.sleep(random.randint(5, 8))
    elem = browser.find_element(By.XPATH, '//*[@id="paymentCheckbox-101"]') # cash/card (when collected)
    browser.execute_script("arguments[0].click();", elem)

    time.sleep(random.randint(5, 8))
    browser.find_element(By.XPATH, '//*[@id="confirmOrder2Button"]/span').click() # continue

    try:
        time.sleep(random.randint(4, 6))
        browser.find_element(By.XPATH, '//*[@id="rootHtml"]/body/div[21]/div[3]/div/button').click() # click on close button
    except:
        pass

    time.sleep(random.randint(5, 8))
    email_section = browser.find_element(By.XPATH, '//*[@id="userEmail"]') # find email section
    email_section.clear()
    email_section.send_keys(email + Keys.ENTER) # Insert email address

    time.sleep(random.randint(4, 8))
    phone_section = browser.find_element(By.XPATH, '//*[@id="inpTelNumber"]') # find phone section
    phone_section.send_keys(phone + Keys.ENTER) # Insert phone number

    time.sleep(random.randint(4, 6))
    browser.find_element(By.XPATH, '//*[@id="order3-footer-container"]/div[1]/a[2]/span[1]').click() # finish order
    

time.sleep(20)
print('Program finished!')
