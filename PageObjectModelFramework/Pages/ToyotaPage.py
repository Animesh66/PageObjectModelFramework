from PageObjectModelFramework.Pages.BasePage import BasePage
from PageObjectModelFramework.Utilities import configReader


class ToyotaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
