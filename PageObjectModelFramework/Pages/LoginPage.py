from selenium.webdriver.support.select import Select

from PageObjectModelFramework.Pages.BasePage import BasePage
from PageObjectModelFramework.Utilities import configReader


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def doLogin(self):
        pass