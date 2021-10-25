def AvtoTestMetro():
    import uiautomator2 as u2
    from time import sleep
    from datetime import datetime
    import requests

    chatId = '-1001609151514'
    TOKEN = '2066274978:AAGZuRG2RMvyUPtOpArDN6AxhrdpXFY4NYk'

    def SendMessage(text):
        requests.get(
            f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chatId}&text={text}')

    def send_screencast(video, text):
        files = {'video': open(video, 'rb')}
        requests.post(f'https://api.telegram.org/bot{TOKEN}/sendVideo?chat_id={chatId}&caption={text}', files=files)

    def NowDateVideo():
        now = datetime.now().strftime("%d_%m_%Y(%H_%M)")
        return now

    def NowDate():
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return now

    def BrowserExit():
        d.click(1000, 200)
        sleep(1)
        d.shell('input touchscreen swipe 930 880 380 880')
        sleep(1)
        d.press("home")

    def CheckInternet():
        d.press("home")
        sleep(2)
        d.shell("am start -a android.intent.action.VIEW  https://www.google.com/")
        sleep(5)
        GOOGLE = d.xpath('//*[@resource-id="hplogo"]')
        GOOGLE.wait(5)
        print("Иконка Гугла: ", GOOGLE.exists)
        if GOOGLE.exists:
            print(f"{NowDate()}  Доступ в интернет есть!")
            SendMessage(f"📣 {SSID}: Доступ в интернет есть! ✅ ")
            BrowserExit()
            return True
        else:
            print(f"{NowDate()}  Доступа в интернет нет!")
            SendMessage(f"📣 {SSID}: Доступа в интернет нет! :( ")
            BrowserExit()
            return False

    SSID = '_P_metro'
    SsidNameVideo = 'P_metro'
    p = NowDateVideo()
    d = u2.connect()
    flag = 3
    flag2 = 10

    try:
        SendMessage("📣Автотесты запущены🚀")  # Отправка сообщения в телеграмм канал
        if d.info.get('screenOn'):
            d.shell('input keyevent 26')  # Проверка активности экрана. Если активен, то выключится перед началом теста
        d.shell('input keyevent 26 && input touchscreen swipe 930 880 930 380')  # Разблокировка экрана
        d.shell(
            "am start -n com.android.settings/com.android.settings.wifi.WifiSettings")  # Переход в настройки устройства
        WIFI = d(text='Wi-Fi', className='android.widget.TextView')
        WIFI.click_exists(3)
        d.shell('svc wifi enable')  # Включение Wi-Fi
        d.screenrecord(f"screencasts/{p}_{SsidNameVideo}.mp4")  # Запуск записи экрана

        # -- Подключение к SSID
        SsidName = d(text=f'{SSID}', className='android.widget.CheckedTextView')
        print(SsidName.get_text())
        SsidName.click_exists(20)
        print(f"{NowDate()}  SSID найден.Авторизация началась")
        sleep(3)
        # -- Проверка взлёта кептива
        Captive = d(text="Подключаться автоматически")
        if Captive.exists:
            print(f"{NowDate()}  Кептив открылся")
        else:
            print(f"{NowDate()}  Кептив не отработал.Тест завершен.")
            quit()
        # -- Нажатие на "Войти в интернет"
        while flag != 0:
            OpenSixtyMin = d(text='Войти на 60 минут')
            if OpenSixtyMin.exists:
                sleep(2)
                # кнопка находится но неактивна в течении 5 сек. Нужен кликабле
                OpenSixtyMin.click(2)
                print(f"{NowDate()}  Нажата кнопка 'Войти в интернет'")
                sleep(3)
                break
            if flag == 1:
                print(f"{NowDate()} Кнопка 'Войти в интернет' не найдена. Скрипт принудительно завершен ")
                quit()
            else:
                flag -= 1
                print(flag)
                sleep(3)
                continue
        # -- Прохождение рекламы
        ButtonX1 = d.xpath(
            '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
        ButtonX2 = d.xpath(
            '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]')
        ButtonX3 = d.xpath('// *[ @ resource - id = "app"] / android.view.View[1] / android.view.View[3]')
        Next = d(text="Продолжить", className='android.widget.Button')
        Continue = d(text="Далее", className='android.widget.Button')

        for i in range(20):
            print("Кнопка ButtonX1", ButtonX1.exists)
            print("Кнопка ButtonX2", ButtonX2.exists)
            if Next.exists or Continue.exists:
                print('вышел из цикла')
                break
            if ButtonX1.exists:
                ButtonX1.click_exists(5)
                print(f"{NowDate()}  Нажат крестик вид №1")
                sleep(4)
            elif ButtonX2.exists:
                ButtonX2.click_exists(5)
                print(f"{NowDate()}  Нажат крестик вид №2")
                sleep(4)
            elif flag2 == 1:
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

        FinalCheck = d(description="cabinet.wi-fi")
        while not FinalCheck.exists:
            print(FinalCheck.exists)
            if ButtonX1.exists:
                ButtonX1.click_exists(5)
                print(f"{NowDate()}  Нажат крестик вид №1")
                sleep(5)
            elif ButtonX2.exists:
                ButtonX2.click_exists(5)
                print(f"{NowDate()}  Нажат крестик вид №2")
                sleep(5)
            elif ButtonX3.exists:
                ButtonX3.click_exists(5)
                print(f"{NowDate()}  Нажат крестик №5 на портале")
            else:
                print(flag2)
                flag2 -= 1
                print(FinalCheck.exists)
                sleep(5)
                continue

        # тут пока не трогал
        assert FinalCheck.exists, f"{NowDate()}  Авторизация не пройдена.Не найдена кнопка на новостном портале"

        # -- На портале
        Galochka = d(resourceId="android:id/button2")
        Galochka.click_exists(10)
        print(f"{NowDate()}  Нажата галочка")
        CheckInternet()
        SendMessage(f"📣 {SSID}: Автотест пройден ✅ ")
        print(f"{NowDate()}  Автотест пройден ✅")

    except AssertionError:
        print(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале")
        SendMessage(f"🔴 {SSID}: Автотест упал")

    finally:
        sleep(2)
        d.press("home")
        d.screenrecord.stop()
        send_screencast(f"screencasts/{p}_{SsidNameVideo}.mp4", f'{SSID}')
        d.shell('svc wifi disable')
        d.shell('input keyevent 26')
        requests.get("http://sae.msk.vmet.ro/v1/drop/mac/60-ab-67-f7-1d-a0")
        print(f"{NowDate()}  Сессия убита ✅")
