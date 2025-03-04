import time
from driver_setup import get_driver
from element_action import ElementActions
from xpaths import XPATHS

class PlacementPreparation:
    def __init__(self):
        self.driver = get_driver()
        self.actions = ElementActions(self.driver)

    def get_demo(self, url):
        self.driver.get(url)
        try:
            self.actions.click_element(XPATHS["aptitude_dropdown"])
            self.actions.click_element(XPATHS["quantitative_aptitude"])
            self.actions.click_element(XPATHS["number_system"])
            self.actions.click_element(XPATHS["concepts_tab"])
            self.actions.click_element(XPATHS["formulas_tab"])
            self.actions.click_element(XPATHS["questions_btn"])
            self.actions.click_element(XPATHS["view_answer"])
            self.actions.click_element(XPATHS["show_more"])
            self.actions.click_element(XPATHS["checkbox"])
            self.actions.enter_text(XPATHS["comments"], "This is a test comment.")
            time.sleep(4)
            self.actions.click_element(XPATHS["submitbutton"])
            time.sleep(4)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.driver.quit()
