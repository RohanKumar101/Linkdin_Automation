from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome()  


driver.get("https://www.google.com")


driver.get("https://www.linkedin.com/login")


username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
email = os.getenv('email')
username.send_keys(email)  


pword = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password = os.getenv('password')
pword.send_keys(password) 


login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()


time.sleep(5)

print("Login Successful!")


driver.quit()
