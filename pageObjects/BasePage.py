from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

"""
This is the parent class of all other Page Classes 
"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_clicks(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.click()

    def do_sendkeys(self, by_locator, text_to_enter):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ele.send_keys(text_to_enter)

    def get_element_text(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.text

    def is_eleDisplayed(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.is_displayed()

    def mouseClick(self, by_locator1, by_locator2):
        actions = ActionChains(self.driver)
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator1))
        actions.move_to_element(ele).move_to_element(by_locator2).click().perform()

    def select_By_Value_Dropdown(self, by_locator):
        #ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        dropdown = Select(self.driver.by_locator)
        dropdown.select_by_value('4')
        # dropdown.select_by_visible_text('May')
        # dropdown.select_by_index('8')

    def select_By_VisibleText_Dropdown(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        dropdown = Select(self.driver.find_element_by_id(ele))
        dropdown.select_by_visible_text('May')