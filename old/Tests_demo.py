import uiautomator2 as u2
from time import sleep
from Functions.DataName import NowDate

d = u2.connect_usb("a3f47191")
# Fire = d(description="Firefox", clickable="False")
# Fire2 = d.xpath("//android.widget.TextView[@text='Expandable Lists']")
# print(Fire.exists)
# -- Прохождение рекламы
button_x1 = d.xpath(
    '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
button_x2 = d.xpath('//*/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]')

if button_x1.exists:
    button_x1.click_exists(5)
    print(f"{NowDate()}  Нажат крестик вид №1")
elif button_x2.exists:
    button_x2.click_exists(5)
    print(f"{NowDate()}  Нажат крестик вид №2")

# driver.findElementsByAndroidUIAutomator("new UiSelector().clickable(true)").size());
