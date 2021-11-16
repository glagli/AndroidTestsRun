def AvtoTestMetro (ser, MAC, DevicesName, ssid):
    import uiautomator2 as u2
    from time import sleep
    import requests
    import Functions.CheckInternet
    from Functions.DataName import NowDate
    from Functions.TelegramApi import SendMessage
    from Functions.LockDisplay import Lock
    from Functions.Sumsung import Connect_WiFi
    from Functions import Schet

    with open("buttonClick.txt", 'a+', encoding='utf-8') as f:

        if DevicesName == "Samsung A32":
            ssid = ssid
            name_video = ssid[1::]
        else:
            ssid = ssid
            name_video = ssid[1::]

        d = u2.connect_usb(ser)
        flag = 7
        flag2 = 10
        err400 = False

        try:
            print(f'Тест № {Schet.count}')
            print(f"{NowDate()}  {DevicesName}: 📣 {ssid}:  Автотест запущен📱")
            f.write(f"{NowDate()}  {DevicesName}: 📣 {ssid}:  Автотест запущен🚀\n")

            if d.info.get('screenOn'):
                d.shell('input keyevent 26')  # Проверка активности экрана. Если активен, то выключится перед началом теста
            Lock(d)  # Разблокировка экрана

            if DevicesName == "Samsung A32":
                Connect_WiFi(d)
            else:
                d.shell("am start -n com.android.settings/com.android.settings.wifi.WifiSettings")  # Переход в настройки
                WIFI = d(text='Wi-Fi', className='android.widget.TextView')
                WIFI.click_exists(3)

            d.shell('svc wifi enable')  # Включение Wi-Fi
            sleep(8)

            # -- Подключение к SSID
            if DevicesName == "Samsung A32":
                # SsidName = d.xpath(f'//*[@text="{ssid}"]')
                SsidName = d(resourceId="com.android.settings:id/title", text=f"{ssid}")
                # SsidName.click_exists(20)
                SsidName.click_gone(5, 5)
                # sleep(7)
                # SsidName.click_exists(5)
                sleep(6)

            else:
                SsidName = d(text=f'{ssid}', className='android.widget.CheckedTextView')
                # SsidName.click_exists(20)
                SsidName.click_gone(5, 5)
                sleep(7)


            # -- Проверка взлёта кептива
            if DevicesName == "Samsung A32":
                Captive = d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[1]')
            else:
                Captive = d(text="Подключаться автоматически")

            Captive.wait(15)
            if Captive.exists:
                print(f"{NowDate()}  Кептив открылся")
                f.write(f"{NowDate()}  Кептив открылся\n")
            elif not SsidName.exists:
                print(f"{NowDate()}  SSID не найден.Тест завершен.")
                f.write(f"{NowDate()}  SSID не найден.Тест завершен.\n")
                SendMessage(f"{DevicesName}: ⛔ {ssid}: SSID не найден")
                return
            else:
                if Functions.CheckInternet.CheckInternet(d, DevicesName):
                    print(f"{NowDate()}  Предыдущая сессия не убита.Тест завершен.")
                    f.write(f"{NowDate()}  Предыдущая сессия не убита.Тест завершен.\n")
                    SendMessage(f"{DevicesName}: ⛔ {ssid}: Сессия не убита")
                else:
                    print(f"{NowDate()}  Кептив не отработал.Тест завершен.")
                    f.write(f"{NowDate()}  Кептив не отработал.Тест завершен.\n")
                    SendMessage(f"{DevicesName}: 🔥 {ssid}: Автотест упал")
                return

            # -- Чекер ошибки 400
            if d(text="Error 400: Bad Request").exists:
                # -- Подключение к ssid
                d.shell("am start -a android.intent.action.VIEW  http://gowifi.ru")
                print(f"{NowDate()}  Error 400: Bad Request")
                f.write(f"{NowDate()}  Error 400: Bad Request\n")
                print(f"{NowDate()}  Авторизация через браузер")
                f.write(f"{NowDate()}  Авторизация через браузер\n")
                err400 = True
                sleep(5)

            # -- Нажатие на "Войти в интернет"
            while flag != 0:
                OpenSixtyMin = d(text='Войти в Интернет')
                if OpenSixtyMin.exists:
                    sleep(2)
                    # кнопка находится но неактивна в течении 5 сек. Нужен кликабле
                    OpenSixtyMin.click_gone()
                    print(f"{NowDate()}  Нажата кнопка 'Войти в Интернет'")
                    f.write(f"{NowDate()}  Нажата кнопка 'Войти в Интернет'\n")
                    sleep(7)
                    break
                if flag == 1:
                    print(f"{NowDate()}  Кнопка 'Войти в Интернет' не найдена. Скрипт принудительно завершен ")
                    f.write(f"{NowDate()}  Кнопка 'Войти в Интернет' не найдена. Скрипт принудительно завершен \n")
                    return
                else:
                    flag -= 1
                    sleep(3)
                    continue
            # -- Прохождение рекламы
            ButtonX1 = d.xpath(
                '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
            ButtonX2 = d.xpath(
                '//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]')



            final_check2 = d(description="cabinet.wi-fi")
            final_check = d.xpath('//*[@text="cabinet.wi-fi"]')
            while not (final_check.exists or final_check2.exists):
                if ButtonX1.exists:
                    ButtonX1.click_exists(5)
                    print(f"{NowDate()}  Нажат крестик вид №1")
                    f.write(f"{NowDate()}  Нажат крестик вид №1\n")
                    sleep(5)
                elif ButtonX2.exists:
                    if DevicesName == "XiaomiMi9":
                        ButtonX2.click_exists(5)
                        # d.click(954, 500)
                    if DevicesName == "XiaomiRedmiNote9":
                        d.click(980, 490)
                    if DevicesName == "Samsung A32" and err400:
                        ButtonX2.click_exists(5)
                    if DevicesName == "Samsung A32" and err400 == False:
                        d.click(962, 273)
                    print(f"{NowDate()}  Нажат крестик вид №2")
                    f.write(f"{NowDate()}  Нажат крестик вид №2\n")
                    sleep(5)
                elif flag2 == 1:
                    print(f"{NowDate()}  Иконка на портале не найдена. Скрипт принудительно завершен ")
                    f.write(f"{NowDate()}  Иконка на портале не найдена. Скрипт принудительно завершен \n")
                    SendMessage(f"{DevicesName}: 🔴 {ssid}: Автотест упал")
                    return
                else:
                    flag2 -= 1
                    sleep(5)
                    continue

            # тут пока не трогал
            assert final_check.exists or final_check2.exists or SsidName.exists, f"{NowDate()}  Авторизация не пройдена.Не найдена кнопка на новостном портале"
            if final_check.exists or final_check2.exists:
                print(f"{NowDate()}  Иконка на портале найдена")
                f.write(f"{NowDate()}  Иконка на портале найдена\n")
            else:
                print(f"{NowDate()}  Иконка на портале не найдена")
                f.write(f"{NowDate()}  Иконка на портале не найдена\n")

            # -- На портале
            if DevicesName != 'Samsung A32' and err400 == False:
                Galochka = d(resourceId="android:id/button2")
                Galochka.click_exists(10)
                print(f"{NowDate()}  Нажата галочка")
                f.write(f"{NowDate()}  Нажата галочка\n")


            if Functions.CheckInternet.CheckInternet(d, DevicesName):
                print(f"{NowDate()}  Доступ в интернет есть!")
                f.write(f"{NowDate()}  Доступ в интернет есть! \n")
            else:
                print(f"{NowDate()} Доступа в интернет нет! Скрипт принудительно завершен ")
                f.write(f"{NowDate()} Доступа в интернет нет! Скрипт принудительно завершен \n")
                SendMessage(f"{DevicesName}: 🔴 {ssid}: Автотест упал.Доступа в интернет нет!")
                return

            SendMessage(f"{DevicesName}: 📣 {ssid}: Автотест успешно пройден ✅ ")
            print(f"{NowDate()}  Автотест пройден ✅")
            f.write(f"{NowDate()}  Автотест пройден ✅ \n")

        except AssertionError:
            print(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале")
            f.write(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале\n")
            SendMessage(f"{DevicesName}: 🔴 {ssid}: Автотест упал")

        finally:
            sleep(1)
            d.press("home")
            d.shell('svc wifi disable')
            d.shell('input keyevent 26')
            requests.get(f"http://sae.msk.vmet.ro/v1/drop/mac/{MAC}")
            print(f"{NowDate()}  Сессия убита ✅")
            print(f"_____________________________________________________________")
            f.write(f"{NowDate()}  Сессия убита ✅\n")
            f.write(f"_____________________________________________________________\n")
            Schet.count += 1
            sleep(10)
