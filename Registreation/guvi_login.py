import time
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

client = pymongo.MongoClient("mongodb://localhost:27017/") 
db = client["user_database"]  
collection = db["credentials"]  

def fetch_credentials():
    return list(collection.find({}, {"_id": 0, "email": 1, "password": 1}))

def login(email, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    
    try:
        wait = WebDriverWait(driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='login-btn']")))
        login_button.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(password)
        checkbox_button =  wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='logged-in']")))
        checkbox_button.click()
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='login-btn']")))
        login_btn.click()
        time.sleep(7)
        print(f"Login successful for {email}")
    except Exception as e:
        print(f"Login failed for {email}: {e}")
    finally:
        driver.quit()

credentials = fetch_credentials()
for cred in credentials:
    login(cred["email"], cred["password"])
