import pytest
from pages.links import Links


@pytest.mark.skip
def test_windows_tab(browser):
    links = Links(browser)
    links.visit()

    assert links.home_link.exist()
    assert links.home_link.get_text() == 'Home'
    assert links.home_link.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) == 1
    links.home_link.click()
    assert len(browser.window_handles) == 2

