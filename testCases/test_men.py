import time

import allure
import pytest

from commonUtilities.customLogger import LogHelper
from commonUtilities.readConfigProperty import Readconfig
from pageObjects import LoginPage
from pageObjects.MenPage import MenPage
from pageObjects.LoginPage import Login
from testCases.BaseTest import BaseTest

@allure.severity(allure.severity_level.NORMAL)
class Test_MenPage(BaseTest):
    baseURL = Readconfig.getApplicationUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogHelper.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip("This functionality is not yet developed")
    @pytest.mark.sanity
    def test_Testcase001(self):
        self.logger.info("=====test_loginToApplication======")
        self.logger.info("Loging to Application")
        self.driver.get(self.baseURL)
        self.lpage = Login(self.driver)
        self.lpage.clickOnLoginBtn()
        self.logger.info("Clicking on Login link")
        self.lpage.do_login(self.username, self.password)

        self.mPage = MenPage(self.driver)
        time.sleep(5)
        self.mPage.clickOnMenLinks()
        self.logger.info("Clicking on Men Link")

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Testcases002(self):
        self.logger.info("test_Testcases002")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_Testcases003(self):
        self.logger.info("test_Testcases003")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_Testcases004(self):
        self.logger.info("test_Testcases004")