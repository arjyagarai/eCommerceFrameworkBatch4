import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import Login
from commonUtilities.readConfigProperty import Readconfig
from commonUtilities.customLogger import LogHelper
import time

from testCases.BaseTest import BaseTest


class Test_login_01(BaseTest):
    baseURL = Readconfig.getApplicationUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    # cname = Readconfig.getConfigforPayementDetails('customername')
    # cardno = Readconfig.getConfigforPayementDetails('creditcard')

    logger = LogHelper.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_homePageTitle(self):
        self.logger.info("=====test_homePageTitle======")
        self.logger.info("Verifying HomePageTitle")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        exp_title = 'Online Shopping for Men, Women Clothing & Accessories at Bewakoof'
        if act_title == exp_title:
            self.logger.info("HomePageTitle testcase is passed")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="LoginPageTitleScreenshot",
                          attachment_type= AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error("HomePageTitle testcase is failed")
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_loginToApplication(self):
        self.logger.info("=====test_loginToApplication======")
        self.logger.info("Loging to Application")
        self.driver.get(self.baseURL)
        self.lpage = Login(self.driver)
        self.lpage.clickOnLoginBtn()
        self.logger.info("Clicking on Login link")
        self.lpage.do_login(self.username, self.password)
        is_displayed = self.lpage.userIconDisplayed()
        assert is_displayed
        self.logger.info("======Execution has been completed=======")



