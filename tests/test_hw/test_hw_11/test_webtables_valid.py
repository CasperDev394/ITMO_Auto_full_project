import time

from pages.tables import Tables


def test_webtables_valid_dialog(browser):

    tables = Tables(browser)
    tables.visit()

    assert tables.btn_add.exist()
    tables.btn_add.click()
    assert tables.modal_dialog.visible()

    tables.submit.click()
    assert tables.modal_dialog.visible()

    assert 'tester@ttt.tt' not in tables.table.get_text()
    tables.fill_form()
    # time.sleep(3)
    tables.submit.click()
    assert not tables.modal_dialog.exist()
    # time.sleep(3)

    assert 'tester@ttt.tt' in tables.table.get_text()

    tables.btn_edit_4.click()
    assert tables.inp_mail.get_dom_attribute('value') == 'tester@ttt.tt'
    # time.sleep(3)

    tables.inp_mail.clear()
    tables.inp_mail.send_keys('tester-new@ttt.tt')
    tables.submit.click()
    assert 'tester-new@ttt.tt' in tables.table.get_text()

    tables.btn_delete_4.click()
    assert 'tester-new@ttt.tt' not in tables.table.get_text()


def test_webtables_next(browser):

    tables = Tables(browser)
    tables.visit()

    tables.rows_5.click()

    assert tables.btn_next.get_dom_attribute('disabled')
    assert tables.btn_prev.get_dom_attribute('disabled')

    for i in range(3):
        tables.btn_add.click()
        tables.fill_form()
        tables.submit.click()

    assert tables.total_page.get_text() == '2'
    assert not tables.btn_next.get_dom_attribute('disabled')
    # time.sleep(3)

    tables.btn_next.click()
    assert tables.current_page.get_dom_attribute('value') == '2'
    tables.btn_prev.click()
    assert tables.current_page.get_dom_attribute('value') == '1'
    # time.sleep(3)
