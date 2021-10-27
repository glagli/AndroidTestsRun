from time import sleep


def BrowserMiuiExit (d):
    d.click(1000, 200)
    sleep(1)
    clouseAll = d(resourceId="com.mi.globalbrowser:id/nav_close_all")
    assert clouseAll, "Не найдена кнопка закрытия вкладок браузера"
    clouseAll.click(2)
    # d.shell('input touchscreen swipe 930 880 380 880')
    sleep(1)
    clouseButton = d(resourceId="android:id/button1")
    assert clouseButton, "Не найдена кнопка подтвержения закрытия вкладок браузера"
    clouseButton.click(2)
    sleep(1)
    d.press("home")


def BrowserChromeExit (d):
    d(resourceId="com.android.chrome:id/tab_switcher_button").click(2)
    sleep(1)
    d.xpath('//*[@resource-id="com.android.chrome:id/tab_switcher_toolbar"]/android.widget.LinearLayout[2]').click(2)
    sleep(1)
    d(resourceId="com.android.chrome:id/menu_item_text", text="Закрыть все вкладки").click(2)
    sleep(1)
    d.press("home")
