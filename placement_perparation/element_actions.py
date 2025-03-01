from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ElementActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, xpath):
        """Waits for an element to be clickable and clicks it."""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
