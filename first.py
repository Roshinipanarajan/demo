
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.guvi.in/")
# driver.find_element(By.ID,"login-btn").click()
# driver.find_element(By.ID,"email").send_keys("gandhamathan@guvi.in")
# driver.find_element(By.ID,"password").send_keys("Gandha9499@")
# driver.find_element(By.ID,"login-btn").click()
# # driver.find_element(By.CSS_SELECTOR, "img.bg-base-100").click()
# driver.back()

# time.sleep(5)
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
# driver.get("https://www.guvi.in/")
# time.sleep(2)  
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# driver.find_element(By.ID, "email").send_keys("gandhamathan@guvi.in")
# driver.find_element(By.ID, "password").send_keys("Gandha9499@")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3) 
# banner = driver.find_element(By.CSS_SELECTOR, "img[title='Republic-offer-2025']")
# banner.click()
# time.sleep(3)  
# driver.back()
# time.sleep(3)  
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()

# driver.get("https://www.guvi.in/")
# driver.find_element(By.ID, "login-btn").click()

# driver.find_element(By.ID, "email").send_keys("gandhamathan@guvi.in")
# driver.find_element(By.ID, "password").send_keys("Gandha9499@")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(5) 
# banners = driver.find_elements(By.CSS_SELECTOR, "img.bg-base-100")
# for banner in banners:
#     try:
#         driver.execute_script("arguments[0].scrollIntoView();", banner)
#         time.sleep(2)
#         driver.execute_script("arguments[0].click();", banner)
#         time.sleep(5) 
#         original_window = driver.current_window_handle
#         all_windows = driver.window_handles

#         for window in all_windows:
#             if window != original_window:
#                 driver.switch_to.window(window)
#                 time.sleep(5) 
#                 print("Redirected to:", driver.current_url)
#                 driver.close()
#                 driver.switch_to.window(original_window)
#                 break  
#         time.sleep(10)  

#     except Exception as e:
#         print("Error clicking banner:", str(e))
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# # Setup driver
# driver = webdriver.Chrome()
# driver.get("https://www.guvi.in/")

# try:
#     # Wait and click login button
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

#     # Enter credentials
#     driver.find_element(By.ID, "email").send_keys("gandhamathan@guvi.in")
#     driver.find_element(By.ID, "password").send_keys("Gandha9499@")
    
#     # Click login button
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

#     # Wait for the redirection to complete
#     time.sleep(5)

#     # Ensure the page is redirected to https://www.guvi.in/
#     expected_url = "https://www.guvi.in/"
#     current_url = driver.current_url

#     if current_url != expected_url:
#         print(f"Unexpected redirection to: {current_url}. Redirecting back to {expected_url}.")
#         driver.get(expected_url)
#         time.sleep(3)  # Wait for the page to load

#     print("Successfully redirected to:", driver.current_url)

#     # Now proceed with banner clicking
#     banners = driver.find_elements(By.CSS_SELECTOR, "img.bg-base-100")

#     for banner in banners:
#         try:
#             driver.execute_script("arguments[0].scrollIntoView();", banner)
#             time.sleep(2)
#             driver.execute_script("arguments[0].click();", banner)
#             time.sleep(5)

#             original_window = driver.current_window_handle
#             all_windows = driver.window_handles

#             for window in all_windows:
#                 if window != original_window:
#                     driver.switch_to.window(window)
#                     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#                     print("Redirected to:", driver.current_url)
#                     driver.close()
#                     driver.switch_to.window(original_window)
#                     break  

#         except Exception as e:
#             print("Error clicking banner:", str(e))

# except NoSuchElementException as e:
#     print("Error finding elements:", str(e))

# finally:
#     driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.guvi.in/")
# driver.find_element(By.ID, "login-btn").click()
# driver.find_element(By.ID, "email").send_keys("gandhamathan@guvi.in")
# driver.find_element(By.ID, "password").send_keys("Gandha9499@")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(5)
# driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()
# driver.maximize_window()

# # Navigate to Guvi
# driver.get("https://www.guvi.in/")

# # Click on the login button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

# # Enter login credentials
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("gandhamathan@guvi.in")
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Gandha9499@")

# # Click on login button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

# # Wait for the profile picture to appear, indicating successful login
# try:
#     profile_icon = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "⭐️ozkxx5-0"))
#     )
#     print("Login successful. Redirected to profile page.")
# except:
#     print("Login failed or profile page not loaded.")

# # Quit the driver
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.guvi.in/")
# driver.find_element(By.ID,"login-btn").click()
# driver.find_element(By.ID,"email").send_keys("gandhamathan@guvi.in")
# driver.find_element(By.ID,"password").send_keys("Gandha9499@")
# driver.find_element(By.ID,"login-btn").click()

# # Wait for the profile picture to appear, ensuring a successful login
# try:
#     profile_icon = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "⭐️ozkxx5-0"))
#     )
#     print("Login successful. Profile icon detected.")
# except:
#     print("Login failed or profile icon not found.")

# # Ensure we are still on the homepage
# if driver.current_url != "https://www.guvi.in/":
#     print("Redirected to another page. Navigating back to homepage...")
#     driver.get("https://www.guvi.in/")  # Redirect back to homepage

# # Wait to confirm we are on the correct page
# time.sleep(5)

# # Quit the driver
# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

# Open the target website
driver.get("https://www.guvi.in/courses/?current_tab=myCourses")
time.sleep(5)

# Locate the "Paid Courses" tab and click it
paid_courses_tab = driver.find_element(By.XPATH, "//div[contains(@class, 'courses-tab') and contains(@class, 'activeTab') and text()='Paid Courses']")
paid_courses_tab.click()
driver.quit()
