from time import sleep
from Functions.DataName import NowDate
from Functions.Browser import BrowserExit
from Functions.Browser import SamsungExit


def CheckInternet (d, DevicesName):
    d.press("home")
    sleep(2)
    d.shell("am start -a android.intent.action.VIEW  https://www.google.com/")
    sleep(5)
    google = d.xpath('//*[@resource-id="hplogo"]')
    google.wait(5)
    # print(f"{NowDate()}  Иконка Гугла:", google.exists)
    if google.exists:
        if DevicesName == "Samsung A32":
            SamsungExit(d)
        else:
            BrowserExit(d)
        return True
    else:
        if DevicesName == "Samsung A32":
            SamsungExit(d)
        else:
            BrowserExit(d)
        return False
