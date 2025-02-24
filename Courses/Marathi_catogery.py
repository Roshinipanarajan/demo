import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://staging.qwik-guvi.pages.dev/courses/?current_tab=paidcourse")
    wait = WebDriverWait(driver, 30)
    gujarati_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Gujarati')]")))
    gujarati_button.click()
    js_course = wait.until(EC.element_to_be_clickable((By.XPATH, "")))
    js_course.click()
    driver.back()
    python_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Python - IITM Pravartak Certified']")))
    python_course.click()
    driver.back()
    driver.get("https://staging.qwik-guvi.pages.dev/courses/?current_tab=paidcourse")
    time.sleep(5)

finally:
    driver.quit()
    
   