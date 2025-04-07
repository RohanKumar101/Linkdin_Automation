from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import os
import csv
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

profile_urls = [
    'https://www.linkedin.com/in/princeyadav05',
    'https://www.linkedin.com/in/nikhilsharma05',
]

with open('profiles.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Headline'])


    for profile_url in profile_urls:
        driver.get(profile_url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        name_tag = soup.select_one("h1.mnqQoMADCIfVsNsuwkCAAQYLQjpGSdgnKxai.inline.t-24.v-align-middle.break-words")
        name = name_tag.text.strip() if name_tag else "N/A"


        headline_tag = soup.select_one("div.text-body-medium.break-words")
        headline = headline_tag.text.strip() if headline_tag else "N/A"


   
    
      
        print("Name:", name)
        print("Headline:", headline)
     
        writer.writerow([name, headline,])


driver.quit()
