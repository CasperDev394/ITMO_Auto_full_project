import time

from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()
    time.sleep(2)

    for btn in modal_page.btns.find_elements():
        btn.click()
        assert modal_page.modal.exist()
        modal_page.btn_close.click()
        assert not modal_page.modal.exist()




