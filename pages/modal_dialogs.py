from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.path_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.path_url)

        self.btn_sidebar_first_child = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')

        self.smallModal = WebElement(driver, '#showSmallModal')
        self.largeModal = WebElement(driver, '#showLargeModal')
        self.btns = WebElement(driver, '#modalWrapper > div > button')
        self.modal = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close = WebElement(driver, 'div.modal-header > button')
