import pytest

from pages.text_box import TextBox
import allure


def test_placeholder(browser):
    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.name.get_dom_attribute('placeholder') == 'Full Name'

