'''
This code automates payment journey for a specific product on Ajio website.
It starts with adding the product to the bag, then logging in to the site, and proceeding for payment.
Payment is done through Paytm wallet which takes debit/credit card information and an OTP.

'''

import sys 

phone_number = sys.argv[1]
card_number = sys.argv[2]
expiry_month = sys.argv[3]
expiry_year = sys.argv[4]
cvv = sys.argv[5]

#importing required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

#read_otp_from_phone is a function written for reading otp on windows from messages received on android phone.
from read_otp import read_otp_from_phone


chrome_driver_path = r'C:\Users\DarothiChowdhury\Desktop\juspay assignment\web_automation\platform-tools_r34.0.3-windows\chromedriver_win32\chromedriver'

service = Service(chrome_driver_path)

options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

#initializing webdriver
driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

#this is the product page on ajio which we will using for payment automation walk through
url = "https://www.ajio.com/giordano-gt02-bk-digital-watch-with-stainless-steel-strap/p/4932390750_multi"
driver.get(url)

time.sleep(5) 
driver.maximize_window()
wait = WebDriverWait(driver, 5) 
time.sleep(5) 

#here we add the produc to bag
add_to_bag = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[9]/div[1]/div[1]/div').click()
time.sleep(2) 
wait = WebDriverWait(driver, 3) 

#now we go to the bag
go_to_bag = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/div[2]/a/div').click()
wait = WebDriverWait(driver, 3)

#we proceed for payment 
proceed = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/button').click()
wait = WebDriverWait(driver, 3) 
time.sleep(2)

#but before payment, we will need to login to our ajio account
login_number = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/header/div[1]/div[1]/ul/li[1]/div/div/div/div[2]/div/form/div[2]/div[1]/label/input').send_keys(phone_number)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/header/div[1]/div[1]/ul/li[1]/div/div/div/div[2]/div/form/div[2]/div[2]/input').click()

time.sleep(12)
#now we enter the otp received on phone
otp = read_otp_from_phone().split()[1]
wait = WebDriverWait(driver, 3) 
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/header/div[1]/div[1]/ul/li[1]/div/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/input').send_keys(otp)
time.sleep(10)
wait = WebDriverWait(driver, 5) 
start_shopping = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/header/div[1]/div[1]/ul/li[1]/div/div/div/div[2]/div/div/div[2]/form/div[2]/input').click()
time.sleep(10)

#we now procedd to shipping
driver.find_element(By.XPATH, '//button[text()="Proceed to shipping"]').click()
# proceed_shipping = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[2]')
# driver.execute_script("arguments[0].click();", proceed_shipping)
time.sleep(2)

#payment 
proceed_payment = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div[2]/div[2]')
driver.execute_script("arguments[0].click();", proceed_payment)
time.sleep(5)

#selecting paytm wallet
wallet = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[1]/div[3]/div").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)
paytm = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div").click()
time.sleep(2)
pay = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/form/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[1]/label/input").click()
time.sleep(2)

#putting in card information
card_number = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[2]/div/section/div/div[2]/div[2]/div[1]/div[1]/div/div/input').send_keys(card_number)
month = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/input[1]').send_keys(expiry_month)
year = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/input[2]').send_keys(expiry_year)
cvv = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[2]/div/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/input').send_keys(cvv)
sumbit = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[3]/div/div[2]/div/section[1]/div[2]/div[2]/div/section/div/div[2]/div[2]/div[4]/section/button').click()

time.sleep(10)
driver.close()