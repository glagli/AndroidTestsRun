from Tests import metro
from time import sleep
from Functions.TelegramApi import Send_File
import uiautomator2 as u2
XiaomiMi9 = "be11611b"
MACMi9 = '60-ab-67-f7-1d-a0'

XiaomiRedmiNote9 = "a3f47191"
MACNote9 = '18-87-40-45-D2-9B'


f = open("logs/buttonClick2.txt", 'w', encoding='utf-8')
# for i in range(1):
#     # _P_metro.AvtoTestMetro(XiaomiMi9, MACMi9)
#     metro.AvtoTestMetro(XiaomiRedmiNote9, MACNote9)
#     sleep(5)
if __name__ == "__main__":
    f.close()
    Send_File("logs/buttonClick2.txt")
    # d . open_notification () - шторка с уведомлениями
    # d.open_quick_settings () - шторка с настройками