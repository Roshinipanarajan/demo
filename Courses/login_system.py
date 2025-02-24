import time
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

client = pymongo.MongoClient("mongodb://localhost:27017/") 
db = client["user_database"]  
collection = db["loginsystem"]  

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
        checkbox_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='logged-in']")))
        checkbox_button.click()
        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='login-btn']")))
        login_btn.click()
        time.sleep(5)
        paid_courses_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='keen-slider__slide number-slide0 courses-search-list-carousel-keenslider-top-carousel active']//a[@class='⭐️fr42lf-0 w-full mr-2 flex items-center justify-center text-base md:text-lg font-medium py-2 border rounded-lg language-item'][normalize-space()='English']")))
        paid_courses_tab.click()
        courses_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Node.js']")))
        courses_tab.click()
        time.sleep(9)
        print(f"Login and Paid Courses tab clicked successfully for {email}")

    except Exception as e:
        print(f"Login failed for {email}: {e}")
    finally:
        driver.quit()

credentials = fetch_credentials()
for cred in credentials:
    login(cred["email"], cred["password"])
