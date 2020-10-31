from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":

        chromeOptions = Options()  # Create object of Options
        chromeOptions.add_experimental_option("prefs", {
            "download.default_directory": "C:\\Users\\Admin\\Desktop\\test\\seleniumDownload"})
        driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\test\\chromedriver.exe", options=chromeOptions)

        #driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\test\\chromedriver.exe")

    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\Admin\\Desktop\\test\\geckodriver.exe")
    request.cls.driver = driver
    yield
    driver.close()


#When Scope is Method
@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\Desktop\\test\\chromedriver.exe")
    elif browser =='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Users\\Admin\\Desktop\\test\\geckodriver.exe")
    else:
        driver = webdriver.safari()
    return driver

def pytest_addoption(parser):  # This will get the value from Command Line (CLI)
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setUp method
    return request.config.getoption("--browser")


# PyTest HTML Report adding extra details
def pytest_configure(config):
    config._metadata['Project'] = 'eCommernce bluestone'
    config._metadata['Tester'] = 'PracticeWithArjya'

# To remove some details in HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
