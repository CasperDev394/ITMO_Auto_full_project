from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()
    modal_page.btn_sidebar_first_child.check_count_elements(5)


def test_navigation_modal(browser):
    modal_page = ModalDialogs(browser)
    demo_page = DemoQa(browser)

    modal_page.visit()
    modal_page.refresh()
    modal_page.icon.click()

    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    demo_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
