from pages.elements_page import ElementsPage


def test_find_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_child.check_count_elements(9)

