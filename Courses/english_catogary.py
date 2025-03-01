# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.guvi.in/courses/?current_tab=paidcourse")
# driver.find_element(By.XPATH,"//div[@id='courses-language-filter-common-top']//div[contains(@class, 'language-item') and normalize-space()='Gujarati']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[@href='/courses/gujarati/it-and-software/basics-of-computer']/div[contains(@class, 'card-body')]").click()
# time.sleep(4)


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.guvi.in/courses/?current_tab=paidcourse")

    wait = WebDriverWait(driver, 10)

    # Click on 'Gujarati' language filter
    gujarati_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='courses-language-filter-common-top']//div[contains(text(), 'Gujarati')]")))
    gujarati_filter.click()

  

    # Click on specific course
    course_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/courses/gujarati/it-and-software/basics-of-computer')]")))
    course_element.click()


finally:
    driver.quit()  # Ensure the browser closes after executio