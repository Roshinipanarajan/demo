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
    assemaese_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='keen-slider__slide number-slide12 courses-search-list-carousel-keenslider-top-carousel']//a[@class='⭐️fr42lf-0 w-full mr-2 flex items-center justify-center text-base md:text-lg font-medium py-2 border rounded-lg language-item'][normalize-space()='Marathi']")))
    assemaese_button.click()
    bootstrap_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Bootstrap in Marathi']")))
    bootstrap_course.click()
    time.sleep(8)
    driver.back()
    AI_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Generative AI in Marathi']")))
    AI_course.click()
    driver.back()
    driver.get("https://staging.qwik-guvi.pages.dev/courses/?current_tab=paidcourse")
    time.sleep(5)

finally:
    driver.quit()
    
   