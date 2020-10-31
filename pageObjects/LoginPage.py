from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class Login(BasePage):
    # btn_login_id = "loginLink"
    # textbox_username_id = "mob_email_id"
    # btn_continue_id = "mob_continue_submit"
    # textbox_password_xpath = "//input[@id='mob_password']"
    # btn_logintoaccount_xpath = "//button[@id='mob_continue_submit']"
    # icon_usericon_xpath = "//i[@class='icon_user']"

    # Object Repository - OR
    LOGINLINK = (By.ID, "loginLink")
    USERNAME = (By.ID, "mob_email_id")
    ContinueBtn = (By.ID, "mob_continue_submit")
    PASSWORD = (By.XPATH, "//input[@id='mob_password']")
    LoginBtn = (By.XPATH, "//button[@id='mob_continue_submit']")
    USER_Icon = (By.XPATH, "//i[@class='icon_user']")



    def __init__(self, driver):
        super().__init__(driver)

    def clickOnLoginBtn(self):
        #self.driver.find_element_by_id(self.btn_login_id).click()
        self.do_clicks(self.LOGINLINK)

    def enterUsername(self,username):
        #self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.do_sendkeys(self.USERNAME, username)

    def clickOnContinueBtn(self):
        #self.driver.find_element_by_id(self.btn_continue_id).click()
        self.do_clicks(self.ContinueBtn)

    def enterPassword(self,password):
        #self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
        self.do_sendkeys(self.PASSWORD, password)

    def clickOnLoginToAccountBtn(self):
        #self.driver.find_element_by_xpath(self.btn_logintoaccount_xpath).click()
        self.do_clicks(self.LoginBtn)

    def userIconDisplayed(self):
        #isDisplayed = self.driver.find_element_by_xpath(self.icon_usericon_xpath).is_displayed()
        isDisplayed = self.is_eleDisplayed(self.USER_Icon)
        return isDisplayed

    def do_login(self, username, password):
        self.do_sendkeys(self.USERNAME, username)
        self.do_clicks(self.ContinueBtn)
        self.do_sendkeys(self.PASSWORD, password)
        self.do_clicks(self.LoginBtn)