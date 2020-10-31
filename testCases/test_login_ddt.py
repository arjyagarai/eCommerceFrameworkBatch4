import pytest
from commonUtilities import readConfigProperty, ExcelUtils, customLogger
from commonUtilities.customLogger import LogHelper
from commonUtilities.readConfigProperty import Readconfig
from pageObjects.LoginPage import Login
from testCases.BaseTest import BaseTest

class Test_DDT_Login(BaseTest):
    baseURL = Readconfig.getApplicationUrl()
    path = ".//TestData//TestData.xlsx"
    logger = LogHelper.loggen()

    def test_login_ddt(self):
        self.logger.info("Starting Data Driven Testing")
        self.rows = ExcelUtils.getRowsCount(self.path, 'loginSheet')
        print("Number of rows: ",self.rows)

        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readDataFromExcel(self.path,'loginSheet', r, 1)
            print("Username:", self.username)
            self.password = ExcelUtils.readDataFromExcel(self.path, 'loginSheet', r, 2)
            print("password:", self.password)
            self.driver.get(self.baseURL)
            self.lpage = Login(self.driver)
            self.lpage.clickOnLoginBtn()
            self.logger.info("Clicking on Login link")
            self.lpage.do_login(self.username, self.password)
            self.logger.info(f"Enter username: {self.username} & password: {self.password}")
            is_displayed = self.lpage.userIconDisplayed()
            assert is_displayed

        self.logger.info("======Execution has been completed=======")


