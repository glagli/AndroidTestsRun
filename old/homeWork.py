import uiautomator2 as u2
from time import sleep
import requests
import telebot
import SendMessageChanale
from datetime import datetime

bot = telebot.TeleBot('2066274978:AAGZuRG2RMvyUPtOpArDN6AxhrdpXFY4NYk')


def NowDateVideo():
    now = datetime.now().strftime("%d_%m_%Y(%H_%M)")
    return now


def NowDate():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return now


def ButtonX():
    return d.click(990, 550)


def BrowserExit():
    d.click(1000, 200)
    sleep(2)
    d.shell('input touchscreen swipe 930 880 930 380')  # Разблокировка экрана
    # d.xpath('//*android.widget.ImageButton[1]').click(1)
    sleep(2)
    d.press("home")


def CheckInternet():
    d.press("home")
    sleep(2)
    d.shell("am start -a android.intent.action.VIEW  https://www.google.com/")
    sleep(5)
    GOOGLE = d.xpath('//*[@resource-id="hplogo"]')
    # print(GOOGLE.exists)
    if GOOGLE.exists:
        print(f"{NowDate()}  Доступ в интернет есть!")
        SendMessageChanale.SendMessage(f"📣 {SSID}: Доступ в интернет есть! ✅ ")
        BrowserExit()
        return True
    else:
        print(f"{NowDate()}  Доступа в интернет нет!")
        SendMessageChanale.SendMessage(f"📣 {SSID}: Доступа в интернет нет! :( ")
        BrowserExit()
        return False

    # print(GOOGLE.exists)


p = NowDateVideo()
d = u2.connect()

try:
    # SendMessageChanale.SendMessage("📣Автотесты запущены🚀")  # Отправка сообщения в телеграмм канал
    SSID = '_P_metro'
    SsidVideo = 'P_metro_home'
    flag = 3
    flag2 = 10

    if d.info.get('screenOn'):
        d.shell('input keyevent 26')  # Проверка активности экрана. Если активен, то выключится перед началом теста
    d.shell('input keyevent 26 && input touchscreen swipe 930 880 930 380')  # Разблокировка экрана
    sleep(2)
    # d.screenrecord(f"screencasts/{p}_{SsidVideo}.mp4")  # Запуск записи экрана
    # Для дома эта часть не нужна
    # d.shell("am start -n com.android.settings/com.android.settings.wifi.WifiSettings")  # Переход в настройки устройства
    # sleep(2)
    # WIFI = d(text='Wi-Fi', className='android.widget.TextView')
    # WIFI.click(1)
    # d.shell('svc wifi enable')  # Включение Wi-Fi
    # sleep(5)

    # -- Подключение к SSID

    d.shell("am start -a android.intent.action.VIEW  https://auth.wi-fi.ru/?segment=metro")
    # SsidName = d(text=f'{SSID}', className='android.widget.CheckedTextView')
    # print(SsidName.get_text())
    # SsidName.click(1)
    # print(f"{NowDate()}  SSID найден.Авторизация началась")

    while flag != 0:
        OpenSixtyMin = d(text='Войти на 60 минут')
        if OpenSixtyMin.exists:
            sleep(2)
            # print(f"{NowDate()}  Кептив открылся") -- Можно придумать проверку что кептив взлетел
            # кнопка находится но неактивна в течении 5 сек
            OpenSixtyMin.click(2)
            print(f"{NowDate()}  Нажата кнопка 'Войти в интернет'")
            sleep(2)
            break
        if flag == 1:
            print(f"{NowDate()} Кнопка 'Войти в интернет' не найдена. Скрипт принудительно завершен ")
            quit()
        else:
            flag -= 1
            print(flag)
            sleep(3)
            continue

    # -- Прохождение рекламы --В офисе надо поменять ButtonX1

    Next = d(text="Продолжить", className='android.widget.Button')
    Continue = d(text="Далее", className='android.widget.Button')
    ButtonX1 = d.xpath(
        '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
    ButtonX2 = d.xpath(
        '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]')

    print(Next.exists)
    print(Continue.exists)
    for i in range(20):
        if Next.exists or Continue.exists:
            print('вышел из цикла')
            break
        if ButtonX1.exists:
            ButtonX1.click(2)
            print(f"{NowDate()}  Нажат крестик вид №1")
        if ButtonX2.exists:
            ButtonX2.click(2)
            print(f"{NowDate()}  Нажат крестик вид №2")
        if flag2 == 1:
            print(f"{NowDate()} Кнопка 'Далее или Продолжить' не найдена. Скрипт принудительно завершен ")
            quit()
        else:
            print(flag2)
            flag2 -= 1
            print(Next.exists)
            print(Continue.exists)
            sleep(4)
            continue


    if Next.exists:
        Next.click(1)
        print(f"{NowDate()}  Нажата кнопка Продолжить")
    else:
        Continue = d(text="Далее", className='android.widget.Button')
        Continue.click()
        print(f"{NowDate()}  Нажата кнопка Далее")

    sleep(8)
    ButtonX2.click(1)
    print(f"{NowDate()}  Нажат крестик вид №2")
    sleep(8)
    ButtonX1.click(1)
    print(f"{NowDate()}  Нажат крестик вид №1")

    sleep(27)
    ButtonX3 = d.xpath('// *[ @ resource - id = "app"] / android.view.View[1] / android.view.View[3]')
    if ButtonX3.exists:
        ButtonX3.click(2)
        print(f"{NowDate()}  Нажат крестик №5 на портале")
    sleep(3)
    FinalCheck = d(description="cabinet.wi-fi")
    assert FinalCheck.exists, f"{NowDate()}  Авторизация не пройдена.Не найдена кнопка на новостном портале"

    # -- На портале
    Galochka = d(className='android.widget.Button', index=2)
    Galochka.click(1)
    print(f"{NowDate()}  Нажата галочка")
    sleep(2)
    CheckInternet()
    sleep(3)
    SendMessageChanale.SendMessage(f"📣 {SSID}: Автотест пройден ✅ ")
    print(f"{NowDate()}  Автотест пройден ✅")

except AssertionError:
    print(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале")
    SendMessageChanale.SendMessage(f"🔴 {SSID}: Автотест упал")

finally:
    sleep(5)
    BrowserExit()
    d.press("home")
    # d.screenrecord.stop()
    # SendMessageChanale.send_screencast('screencasts/output.mp4', f'{SSID}')
    # d.shell('svc wifi disable')
    d.shell('input keyevent 26')
    # SendMessageChanale.SendMessage(f"📣 {SSID}: Автотест завершен✅")
    # requests.get("http://sae.msk.vmet.ro/v1/drop/mac/60-ab-67-f7-1d-a0")
    # print(f"{NowDate()}  Сессия убита ✅")
