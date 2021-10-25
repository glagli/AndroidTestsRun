import uiautomator2 as u2
from time import sleep

from appium import webdriver
import requests




def BrowserExit ():
    d.click(1000, 200)
    sleep(2)
    d.shell('input touchscreen swipe 930 880 380 880')  # Разблокировка экрана
    sleep(2)
    d.press("home")


def CheckInternet ():
    d.press("home")
    sleep(2)
    d.shell("am start -a android.intent.action.VIEW  https://www.google.com/")
    sleep(5)
    GOOGLE = d.xpath('//*[@resource-id="hplogo"]')
    GOOGLE.wait(5)
    print(GOOGLE.exists)
    if GOOGLE.exists:
        print(f"Доступ в интернет есть!")
        BrowserExit()
        return True
    else:
        print(f"Доступа в интернет нет!")
        BrowserExit()
        return False


d = u2.connect_usb("RF8R40BZQLP")
# d.shell("am start -a android.settings.WIRELESS_SETTINGS")
# d(resourceId="android:id/title", text="Wi-Fi").
d.shell('svc wifi disable')
# d.shell("am start -n com.android.settings/com.android.settings.wifi.WifiSettings")