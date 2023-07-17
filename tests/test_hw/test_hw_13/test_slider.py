import logging

from selenium.webdriver import ActionChains
from pages.slider import Slider
import time
from selenium.webdriver.common.keys import Keys


def test_slider_v2(browser):
    slider = Slider(browser)
    action_chains = ActionChains(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()
    # time.sleep(1)
    action_chains.drag_and_drop_by_offset(slider.slider.find_element(), 0, 1).perform()
    # time.sleep(1)
    assert slider.inp.get_dom_attribute('value') == '50'


def test_slider_v3(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.inp.exist()

    while not slider.inp.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.inp.get_dom_attribute('value') == '50'















