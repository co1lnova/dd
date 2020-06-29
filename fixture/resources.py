from selenium.webdriver.chrome.webdriver import WebDriver
from model.url import auth_page
from fixture.session import SessionHelper
from fixture.document import DocumentHelper
from fixture.navigation import NavigationHelper
from fixture.backend import BackendHelper
from data.assert_data import AssertHelper


class Resources:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.document = DocumentHelper(self)
        self.navigation = NavigationHelper(self)
        self.backend = BackendHelper(self)
        self.assert_data = AssertHelper(self)

    def open_auth_page(self):
        driver = self.driver
        driver.get(auth_page)

    def destroy(self):
        self.driver.close()
