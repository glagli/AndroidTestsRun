import uiautomator2 as u2
from Functions.FindSsid import scroll
from time import sleep

def XiaomiCl(d,DevicesName):
    d.shell("am start -n com.android.settings/.Settings")
    scroll(d,DevicesName)
    sleep(2)
    d.xpath('//*[@text="Приложения"]').click_exists(5)
    d.xpath('//*[@text="Все приложения"]').click_exists(5)
    d(resourceId="android:id/input").click_exists(5)
    d.xpath('//miui.widget.ClearableEditText').send_keys('Html')
    d.press("home")


XiaomiMi9 = "be11611b"
MACMi9 = '60-ab-67-f7-1d-a0'

XiaomiRedmiNote9 = "a3f47191"
MACNote9 = '18-87-40-45-D2-9B'

# Samsung A32
number3 = "RF8R40BZQLP"
MAC3 = '80-9f-f5-9c-71-30'
Name3 = 'Samsung A32'

# d = u2.connect_usb(XiaomiMi9)
d = u2.connect_usb(XiaomiRedmiNote9)
# d = u2.connect_usb(number3)



XiaomiCl(d,'XiaomiRedmiNote9')