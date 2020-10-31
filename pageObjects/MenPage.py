from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class MenPage(BasePage):
    linktxt_men_link = (By.LINK_TEXT, "MEN")
    linktxt_size_link = (By.LINK_TEXT, "M")
    #img_Tshirt_xpath = "//img[@title='Hey There Imposter Half Sleeve T-Shirt Neon Green-Front Bewakoof']"
    img_Tshirt_xpath =  (By.XPATH, "//img[contains(@title,'Half Sleeve T-Shirt Neon')]")

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnMenLinks(self):
        self.do_clicks(self.linktxt_men_link)

    def filterWithSize(self):
        self.do_clicks(self.linktxt_size_link)

    def clickOnTShirt(self):
        self.do_clicks(self.img_Tshirt_xpath)

