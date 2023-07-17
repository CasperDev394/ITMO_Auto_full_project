import time
from pages.alerts import Alerts


def test_check_alert(browser):
    alert = Alerts(browser)
    alert.visit()

    alert.timerAlertButton.click()
    times_temp = 0
    while True:
        time.sleep(1)
        times_temp += 1
        if times_temp == 5:
            assert alert.alert()
            alert.alert().accept()
            break
        else:
            assert not alert.alert()
