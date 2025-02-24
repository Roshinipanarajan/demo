import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.guvi.in/sign-in/")
driver.find_element(By.XPATH,"//a[normalize-space()='Forgot password ?']").click()
time.sleep(6)
driver.quit()