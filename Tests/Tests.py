def AutoTest(ser, mac, devices_name, ssid):
    import uiautomator2 as u2
    from time import sleep
    import requests
    import Functions.CheckInternet
    from Functions.ClearCookie import XiaomiCl
    from Functions.DataName import NowDate
    from Functions.TelegramApi import SendMessage
    from Functions.TelegramApi import Send_screencast
    from Functions.LockDisplay import Lock
    from Functions.Sumsung import Connect_WiFi
    from Functions.FindSsid import scroll

    if devices_name == "Samsung A32" and ssid == 'MT_FREE':
        ssid = ssid
        name_video = ssid
    else:
        ssid = ssid
        name_video = ssid[1::]

    d = u2.connect_usb(ser)
    flag = 5
    flag2 = 10
    err400 = False
    check_err = False

    with open("logs/buttonClick.txt", 'a', encoding='utf-8') as f:
        try:
            print(f"{NowDate()}  {devices_name}: 📣 {ssid}:  Автотест запущен📱")
            f.write(f"{NowDate()}  {devices_name}: 📣 {ssid}:  Автотест запущен🚀\n")
            if d.info.get('screenOn'):
                d.shell('input keyevent 26')  # Проверка активности экрана. Если вкл, то выкл перед началом теста
            Lock(d)  # Разблокировка экрана

            if devices_name == "Samsung A32":
                Connect_WiFi(d)
            else:
                d.shell("am start -n com.android.settings/com.android.settings.wifi.WifiSettings")  # Переход в настр
                wifi = d(text='Wi-Fi', className='android.widget.TextView')
                wifi.click_exists(3)

            d.shell('svc wifi enable')  # Включение Wi-Fi
            d.screenrecord(f"screencasts/{devices_name}_{name_video}.mp4")  # Запуск записи экрана
            sleep(5)

            # -- Подключение к SSID
            if devices_name == "Samsung A32":
                ssid_name = d(resourceId="com.android.settings:id/title", text=f"{ssid}")
                if ssid_name.exists:
                    ssid_name.click_gone(8, 5)
                    sleep(6)
                else:
                    scroll(d, devices_name)
                    sleep(3)
                    ssid_name.click_gone(5, 5)
                    sleep(6)
            else:
                ssid_name = d(text=f'{ssid}', className='android.widget.CheckedTextView')
                if ssid_name.exists:
                    ssid_name.click_gone(8, 5)
                    sleep(7)
                else:
                    scroll(d, devices_name)
                    sleep(3)
                    ssid_name.click_gone(5, 5)
                    sleep(7)

            # -- Проверка взлёта кептива
            if devices_name == "Samsung A32":
                captive = d.xpath('//*[@resource-id="android:id/action_bar"]/android.widget.LinearLayout[1]')
            else:
                captive = d(text="Подключаться автоматически")
            captive.wait(15)
            if captive.exists:
                print(f"{NowDate()}  SSID найден.Авторизация началась")
                f.write(f"{NowDate()}  SSID найден.Авторизация началась\n")
                print(f"{NowDate()}  Кептив открылся")
                f.write(f"{NowDate()}  Кептив открылся\n")
            elif not ssid_name.exists:
                print(f"{NowDate()}  SSID не найден.Тест завершен.")
                f.write(f"{NowDate()}  SSID не найден.Тест завершен.\n")
                SendMessage(f"{devices_name}: ⛔ {ssid}: SSID не найден")
                check_err = True
                return
            else:
                if Functions.CheckInternet.CheckInternet(d, devices_name):
                    print(f"{NowDate()}  Предыдущая сессия не убита.Тест завершен.")
                    f.write(f"{NowDate()}  Предыдущая сессия не убита.Тест завершен.\n")
                    SendMessage(f"{devices_name}: ⛔ {ssid}: Сессия не убита")
                else:
                    print(f"{NowDate()}  Кептив не отработал.Тест завершен.")
                    f.write(f"{NowDate()}  Кептив не отработал.Тест завершен.\n")
                    SendMessage(f"{devices_name}: 🔥 {ssid}: Автотест упал")
                check_err = True
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
                check_err = True
                sleep(5)

            # -- Нажатие на "Войти в интернет"
            if ssid == 'MT_FREE' or ssid == '_P_metro':
                open_sixty_min = d(text='Войти на 60 минут')
            elif ssid == '_P_Sola_Metrotelecom Free':
                open_sixty_min = d(text='Internetga kirish')
            else:
                open_sixty_min = d(text='Войти в Интернет')
            while flag != 0:
                if open_sixty_min.exists:
                    sleep(2)
                    # кнопка находится но неактивна в течении 5 сек. Нужен кликабле
                    open_sixty_min.click_gone(10, 3)
                    print(f"{NowDate()}  Нажата кнопка 'Войти в Интернет'")
                    f.write(f"{NowDate()}  Нажата кнопка 'Войти в Интернет'\n")
                    sleep(6)
                    break
                if flag == 1:
                    print(f"{NowDate()}  Кнопка 'Войти в Интернет' не найдена. Скрипт принудительно завершен ")
                    f.write(f"{NowDate()}  Кнопка 'Войти в Интернет' не найдена. Скрипт принудительно завершен \n")
                    SendMessage(f"{devices_name}: 🔥 {ssid}: Кнопка 'Войти в Интернет' не найдена. Скрипт завершен")
                    check_err = True
                    return
                else:
                    flag -= 1
                    sleep(3)
                    continue

            # -- Прохождение рекламы
            button_x1 = d.xpath('//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
            button_x2 = d.xpath('//*[@text="Авторизация Wi-Fi"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]')

            # До кнопки Продолжить/Далее (Только для метро)
            if ssid == '_P_metro' or ssid == 'MT_FREE':
                button_continue = d(text="Продолжить", className='android.widget.Button')
                button_further = d(text="Далее", className='android.widget.Button')
                err900 = d(text="Ошибка #900")

                for i in range(20):
                    if button_continue.exists or button_further.exists:
                        break
                    if button_x1.exists:
                        button_x1.click_exists(5)
                        print(f"{NowDate()}  Нажат крестик вид №1")
                        f.write(f"{NowDate()}  Нажат крестик вид №1\n")
                        sleep(6)
                    elif button_x2.exists:
                        button_x2.click_exists(5)
                        print(f"{NowDate()}  Нажат крестик вид №2")
                        f.write(f"{NowDate()}  Нажат крестик вид №2\n")
                        sleep(6)
                    elif flag2 == 1:
                        print(f"{NowDate()} Кнопка 'Далее или Продолжить' не найдена.Скрипт принудительно завершен ")
                        f.write(f"{NowDate()} Кнопка 'Далее или Продолжить' не найдена.Скрипт принудительно завершен\n")
                        SendMessage(f"{devices_name}: 🔥 {ssid}: Автотест упал")
                        check_err = True
                        return
                    elif err900.exists:
                        print(f"{NowDate()} Ошибка 900.Скрипт завершен")
                        f.write(f"{NowDate()} Ошибка 900.Скрипт завершен\n")
                        SendMessage(f"{devices_name}: 🔥 {ssid}: Ошибка 900")
                        check_err = True
                        return
                    else:
                        flag2 -= 1
                        sleep(4)
                        continue

                if button_continue.exists:
                    button_continue.click(1)
                    print(f"{NowDate()}  Нажата кнопка Продолжить")
                    f.write(f"{NowDate()}  Нажата кнопка Продолжить\n")
                else:
                    button_further = d(text="Далее", className='android.widget.Button')
                    button_further.click()
                    print(f"{NowDate()}  Нажата кнопка Далее")
                    f.write(f"{NowDate()}  Нажата кнопка Далее\n")
                    sleep(6)

            # Назначения финал чеков для сегментов
            if 'dit' in ssid or ssid == '_P_ttk_hospitals':
                if ssid == '_P_ttk_hospitals':
                    final_check = d(text="mos.ru – Официальный сайт Мэра Москвы")
                    final_check2 = d(text="mos.ru – Официальный сайт Мэра Москвы")
                else:
                    final_check = d.xpath('//*[@content-desc="www.mos"]')
                    final_check2 = d.xpath('//*[@content-desc="www.mos"]')
            elif ssid == '_P_Sola_Metrotelecom Free':
                final_check = d.xpath('//*[@content-desc="Logo"]')
                final_check2 = d.xpath('//*[@content-desc="Logo"]')
            else:
                final_check2 = d(description="cabinet.wi-fi")
                final_check = d.xpath('//*[@text="cabinet.wi-fi"]')

            # Авторизация до новостного портала
            while not (final_check.exists or final_check2.exists or ssid_name.exists):
                if button_x1.exists:
                    button_x1.click_exists(5)
                    print(f"{NowDate()}  Нажат крестик вид №1")
                    f.write(f"{NowDate()}  Нажат крестик вид №1\n")
                    sleep(6)
                elif button_x2.exists:
                    if devices_name == "XiaomiMi9":
                        # d.click(954, 500)
                        button_x2.click_exists(5)
                    if devices_name == "XiaomiRedmiNote9":
                        # d.click(980, 490)
                        button_x2.click_exists(5)
                    if devices_name == "Samsung A32":
                        # d.click(962, 273)
                        button_x2.click_exists(5)
                    print(f"{NowDate()}  Нажат крестик вид №2")
                    f.write(f"{NowDate()}  Нажат крестик вид №2\n")
                    sleep(6)
                elif err900.exists:
                    print(f"{NowDate()} Ошибка 900.Скрипт завершен")
                    f.write(f"{NowDate()} Ошибка 900.Скрипт завершен\n")
                    SendMessage(f"{devices_name}: 🔥 {ssid}: Ошибка 900")
                    check_err = True
                    return
                elif flag2 == 1:
                    print(f"{NowDate()}  Иконка на портале не найдена. Скрипт принудительно завершен ")
                    f.write(f"{NowDate()}  Иконка на портале не найдена. Скрипт принудительно завершен \n")
                    SendMessage(f"{devices_name}: 🔥 {ssid}: Неизвестная ошибка")
                    check_err = True
                    return
                else:
                    flag2 -= 1
                    sleep(5)
                    continue

            # Надо как то упростить
            if 'dit' in ssid or ssid == '_P_ttk_hospitals' or ssid == '_P_Sola_Metrotelecom Free':
                assert final_check.exists or ssid_name.exists, f"{NowDate()}  Авторизация не пройдена.Не найдена " \
                                                               f"кнопка на новостном портале "
                if final_check.exists:
                    print(f"{NowDate()}  Иконка на портале найдена")
                    f.write(f"{NowDate()}  Иконка на портале найдена\n")
                else:
                    print(f"{NowDate()}  Иконка на портале не найдена")
                    f.write(f"{NowDate()}  Иконка на портале не найдена\n")
            else:
                assert final_check.exists or final_check2.exists or ssid_name.exists, f"{NowDate()}  Авторизация не " \
                                                                                      f"пройдена.Не найдена кнопка на" \
                                                                                      f" новостном портале "
                if final_check.exists or final_check2.exists:
                    print(f"{NowDate()}  Иконка на портале найдена")
                    f.write(f"{NowDate()}  Иконка на портале найдена\n")
                else:
                    print(f"{NowDate()}  Иконка на портале не найдена")
                    f.write(f"{NowDate()}  Иконка на портале не найдена\n")

            # -- На портале
            if devices_name != 'Samsung A32':
                tick = d(resourceId="android:id/button2")
                tick.click_exists(10)
                print(f"{NowDate()}  Нажата галочка")
                f.write(f"{NowDate()}  Нажата галочка\n")
            else:
                print(f"{NowDate()}  Кептив закрылся")
                f.write(f"{NowDate()}  Кептив закрылся\n")

            # -- Проверка доступа в интернет
            if Functions.CheckInternet.CheckInternet(d, devices_name):
                print(f"{NowDate()}  Доступ в интернет есть!")
                f.write(f"{NowDate()}  Доступ в интернет есть! \n")
            else:
                print(f"{NowDate()} Доступа в интернет нет! Скрипт принудительно завершен ")
                f.write(f"{NowDate()} Доступа в интернет нет! Скрипт принудительно завершен \n")
                SendMessage(f"{devices_name}: 🔥 {ssid}: Доступа в интернет нет!")
                check_err = True
                return

            # -- Финиш
            SendMessage(f"{devices_name}: 📣 {ssid}: Автотест успешно пройден ✅ ")
            print(f"{NowDate()}  Автотест пройден ✅")
            f.write(f"{NowDate()}  Автотест пройден ✅ \n")

        except AssertionError:
            check_err = True
            print(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале")
            f.write(f"{NowDate()}  🔴 Автотест упал. Не найдена кнопка на новостном портале\n")
            SendMessage(f"{devices_name}: 🔥 {ssid}: Автотест упал")

        finally:
            sleep(2)
            d.screenrecord.stop()
            if err400 and 'Xiaomi' in devices_name:
                XiaomiCl(d, devices_name)
            d.press("home")
            sleep(2)
            d.shell('svc wifi disable')
            d.shell('input keyevent 26')
            requests.get(f"http://sae.msk.vmet.ro/v1/drop/mac/{mac}")
            print(f"{NowDate()}  Сессия убита ✅")
            print(f"_____________________________________________________________")
            f.write(f"{NowDate()}  Сессия убита ✅\n")
            f.write(f"_____________________________________________________________\n")
            sleep(2)
            if check_err:
                Send_screencast(f"screencasts/{devices_name}_{name_video}.mp4", f'Авторизация {devices_name}\n{ssid}')
            sleep(10)
