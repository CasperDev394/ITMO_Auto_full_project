from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.path_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.path_url)

        self.btn_columns = WebElement(driver, 'div[role="columnheader"]')

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, '[title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.submit = WebElement(driver, '#submit')
        self.table = WebElement(driver, 'div.rt-table > div.rt-tbody')
        self.btn_edit_4 = WebElement(driver, '#edit-record-4 > svg')
        self.btn_delete_4 = WebElement(driver, '#delete-record-4 > svg')
        self.rows_5 = WebElement(driver, 'select > option:nth-child(1)')
        self.btn_next = WebElement(driver, '.-next > button')
        self.btn_prev = WebElement(driver, '.-previous > button')
        self.total_page = WebElement(driver, 'span.-totalPages')
        self.current_page = WebElement(driver, 'input[type=number]')

        self.inp_first = WebElement(driver, '#firstName')
        self.inp_last = WebElement(driver, '#lastName')
        self.inp_mail = WebElement(driver, '#userEmail')
        self.inp_age = WebElement(driver, '#age')
        self.inp_salary = WebElement(driver, '#salary')
        self.inp_department = WebElement(driver, '#department')

    def fill_form(self, 
                  inp_first='tester', 
                  inp_last='tester', 
                  inp_mail='tester@ttt.tt', 
                  inp_age='23',
                  inp_salary='5000',
                  inp_department='Development'
                  ):
        self.inp_first.send_keys(inp_first)
        self.inp_last.send_keys(inp_last)
        self.inp_mail.send_keys(inp_mail)
        self.inp_age.send_keys(inp_age)
        self.inp_salary.send_keys(inp_salary)
        self.inp_department.send_keys(inp_department)

