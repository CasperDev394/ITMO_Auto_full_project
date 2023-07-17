from pages.base_page import BasePage
from components.components import WebElement


class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/radio-button'
        self.pageData = {
            'title': 'DEMOQA'
        }
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, '#yesRadio')
        self.impressive = WebElement(driver, '#impressiveRadio')
        self.no = WebElement(driver, '#noRadio')
        self.text = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div:nth-child(2) > p')

