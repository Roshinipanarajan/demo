import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def login(email, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()
    driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='logged-in']").click()
    driver.find_element(By.XPATH, "//a[@id='login-btn']").click()
    time.sleep(7)
    driver.quit()

credentials = [
    ("gandhamathan@guvi.in", "Gandha9499@"),
    ("gandhamathanguvi.in", "Gandha9499@"),   
    ("gandhamathan@guvi.in", "9499@")         
]

for email, password in credentials:
    login(email, password)
    print("have been logged")

