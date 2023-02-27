from selenium import webdriver
import time
# Set the options for Firefox browser
options = webdriver.FirefoxOptions()

# Set the Firefox profile to use
profile_directory = '7x25r0qf.default-release'
options.profile = webdriver.FirefoxProfile(profile_directory)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(options=options)

# Navigate to the provided URL
driver.get('moz-extension://c1dea8f1-5bbe-45fe-9359-b25385ef2454/index.html')
driver.get('moz-extension://c1dea8f1-5bbe-45fe-9359-b25385ef2454/index.html')
print("VPN Connect")
button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/div[2]/div/a/div')))
if button:
        print("hi3")
        button[0].click()

search = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[1]/form/span/input')))
if search:
        print("hi3")
        search[0].send_keys('Spain') 

button = WebDriverWait(driver, 300).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[2]/div[2]/div[3]/div[2]/div/div[2]')))
if button:
        print("hi3")
        button[0].click()

time.sleep(35)        