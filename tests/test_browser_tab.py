import pytest
from pages.browser_tab import BrowserTab
import time


@pytest.mark.skip
def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)

    browser_tab.visit()

    assert len(browser.window_handles) == 1
    browser_tab.new_tab.click()
    # time.sleep(2)
    assert len(browser.window_handles) == 2


