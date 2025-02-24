import time
import pymongo
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["user_database"]
collection = db["register"]

def fetch_register():
    return list(collection.find({}, {"_id": 0, "name": 1, "email": 1, "password": 1, "mobile": 1}))

def validate_password(password):
    return len(password) >= 6 and re.search(r"[0-9]", password) and re.search(r"[a-zA-Z]", password)

def validate_mobile(mobile):
    return bool(re.fullmatch(r"\d{10}", str(mobile)))

def signup(name, email, password, mobile):
    if not validate_password(password):
        print("Skipping {email}: Password does not meet security requirements.")
        return
    if not validate_mobile(mobile):
        print("Skipping {email}: Invalid mobile number.")
        return

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")

    try:
        wait = WebDriverWait(driver, 10)
        signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sign up']")))
        signup_button.click()
        time.sleep(2)  
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys(name)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.ID, "mobileNumber"))).send_keys(mobile)
        signup_btn = wait.until(EC.element_to_be_clickable((By.ID, "signup-btn")))
        signup_btn.click()
        driver.find_element(By.XPATH,"//a[@id='laterBtn']").click()
        time.sleep(6)
        print("Signup successful for {email}")

    except Exception as e:
        print("Signup failed for {email}: {e}")

    finally:
        driver.quit()

register = fetch_register()
for reg in register:
    signup(reg["name"], reg["email"], reg["password"], reg["mobile"])

client.close()

