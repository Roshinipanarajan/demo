import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.guvi.in/courses/?current_tab=paidcourse")
    wait = WebDriverWait(driver, 30)
    odiya_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='courses-language-filter-common-top']//div[@class='⭐️1qsqnp-0 w-full mr-2 flex items-center justify-center text-sm md:text-base font-medium p-2 border rounded-lg text-nowrap language-item active'][normalize-space()='Odiya']")))
    odiya_button.click()
    html_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='py-4 cursor-pointer text-lg no-underline break-keep courses-tab whitespace-nowrap activeTab']")))
    html_course.click()
    driver.back()
    python_course = wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[normalize-space()='Python - IITM Pravartak Certified']")))
    python_course.click()
    driver.back()
    driver.get("https://staging.qwik-guvi.pages.dev/courses/?current_tab=paidcourse")
    time.sleep(5)

finally:
    driver.quit()
    
   