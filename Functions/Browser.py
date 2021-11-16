from time import sleep


def BrowserMiuiExit(d):
    d.click(1000, 200)
    sleep(1)
    clouseAll = d(resourceId="com.mi.globalbrowser:id/nav_close_all")
    if clouseAll.exists:
        clouseAll.click(2)
        sleep(1)
        clouseButton = d(resourceId="android:id/button1")
        if clouseButton.exists:
            assert clouseButton, "Не найдена кнопка подтвержения закрытия вкладок браузера"
            clouseButton.click(2)
            sleep(1)
    d.press("home")


def BrowserChromeExit(d):
    button1 = d(resourceId="com.android.chrome:id/tab_switcher_button")
    if button1.exists:
        button1.click(2)
        sleep(1)
        d.xpath('//*[@resource-id="com.android.chrome:id/tab_switcher_toolbar"]/android.widget.LinearLayout[2]').click(2)
        sleep(1)
        button2 = d(resourceId="com.android.chrome:id/menu_item_text", text="Закрыть все вкладки")
        if button2.exists:
            button2.click(2)
            sleep(1)
    d.press("home")
