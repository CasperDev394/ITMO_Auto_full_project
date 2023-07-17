from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.path_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.path_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, 'textarea#currentAddress')
        self.submit = WebElement(driver, '#submit')

        self.p_name = WebElement(driver, 'p#name')
        self.p_current_address = WebElement(driver, 'p#currentAddress')

