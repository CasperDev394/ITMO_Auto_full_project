from pages.text_box import TextBox


def test_text_box(browser):
    name = 'Boris'
    address = 'SPB'
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys(name)
    text_box.current_address.send_keys(address)
    text_box.submit.click_force()

    assert text_box.p_name.get_text() == 'Name:' + name
    assert text_box.p_current_address.get_text() == 'Current Address :' + address



