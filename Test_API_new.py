from Functions.TelegramApi import Send_File
from Functions.TelegramApi import SendMessage
from Functions.DataName import NowDate
from Tests.Tests import AutoTest


# d.xpath('//*[@text="Подключено"]')
if __name__ == "__main__":
    print(f"{NowDate()}  📣 :  Автотесты запущены📱")
    print(f"_____________________________________________________________")
    with open("logs/buttonClick.txt", 'w', encoding='utf-8') as f:
        f.write(f"{NowDate()}  📣 :  Автотесты запущены🚀\n")
        f.write(f"_____________________________________________________________\n")

    # XiaomiMi9
    number1 = "be11611b"
    MAC1 = '60-ab-67-f7-1d-a0'
    Name1 = 'XiaomiMi9'

    # XiaomiRedmiNote9
    number2 = "a3f47191"
    MAC2 = '18-87-40-45-D2-9B'
    Name2 = 'XiaomiRedmiNote9'

    # Samsung A32
    number3 = "RF8R40BZQLP"
    MAC3 = '80-9f-f5-9c-71-30'
    Name3 = 'Samsung A32'

    SendMessage(f"Автотесты запущены📱")  # Отправка сообщения в телеграмм канал

    # Устренние тесты

    # def startTestsXiaomiRedmi(number, mac, name):
    #     AutoTest(number, mac, name, '_P_metro')
    #     AutoTest(number, mac, name, '_P_cppk')
    #     AutoTest(number, mac, name, '_P_MCC_incarnet')
    #     AutoTest(number, mac, name, '_P_aeroexpress')
    #     AutoTest(number, mac, name, '_p_mvf_bus')
    #     # AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
    #     # ЕОС
    #     AutoTest(number, mac, name, '_P_dit_enforta_street')
    #     AutoTest(number, mac, name, '_P_dit_akado')
    #     AutoTest(number, mac, name, '_P_dit_guest_wifi')
    #     # AutoTest(number, mac, name, '_P_dit_Nauka 3')
    #     # AutoTest(number, mac, name, '_P_dit_snb')
    #     # AutoTest(number, mac, name, '_P_dit_almatel')
    #     # AutoTest(number, mac, name, '_P_dit_beeline')
    #     AutoTest(number, mac, name, '_P_ttk_hospitals')
    #     # AutoTest(number, mac, name, '_P_dit_mts_vdnh')
    #
    #
    # def startTestsXiaomiMi(number, mac, name):
    #     AutoTest(number, mac, name, '_P_metro')
    #     AutoTest(number, mac, name, '_P_cppk')
    #     AutoTest(number, mac, name, '_P_MCC_incarnet')
    #     AutoTest(number, mac, name, '_P_aeroexpress')
    #     AutoTest(number, mac, name, '_p_mvf_bus')
    #     AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
    #     # ЕОС
    #     AutoTest(number, mac, name, '_P_dit_enforta_street')
    #     AutoTest(number, mac, name, '_P_dit_akado')
    #     AutoTest(number, mac, name, '_P_dit_guest_wifi')
    #     AutoTest(number, mac, name, '_P_dit_Nauka 3')
    #     AutoTest(number, mac, name, '_P_dit_snb')
    #     AutoTest(number, mac, name, '_P_dit_almatel')
    #     AutoTest(number, mac, name, '_P_dit_beeline')
    #     AutoTest(number, mac, name, '_P_ttk_hospitals')
    #     AutoTest(number, mac, name, '_P_dit_mts_vdnh')
    #
    #
    # def startTestsSamsung(number, mac, name):
    #     # AutoTest(number, mac, name, 'MT_FREE')
    #     # # AutoTest(number, mac, name, '_P_cppk')  # -- Кептив на самсунге не всплывает
    #     # # AutoTest(number, mac, name, '_P_MCC_incarnet')  # -- Кептив на самсунге не всплывает
    #     # # AutoTest(number, mac, name, '_P_aeroexpress')  # -- Кептив на самсунге не всплывает
    #     # # AutoTest(number, mac, name, '_p_mvf_bus')
    #     AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
    #     # ЕОС
    #     # AutoTest(number, mac, name, '_P_dit_enforta_street')
    #     # AutoTest(number, mac, name, '_P_dit_akado')
    #     # AutoTest(number, mac, name, '_P_dit_guest_wifi')
    #     AutoTest(number, mac, name, '_P_dit_Nauka 3')
    #     AutoTest(number, mac, name, '_P_dit_snb')
    #     AutoTest(number, mac, name, '_P_dit_almatel')
    #     AutoTest(number, mac, name, '_P_dit_beeline')
    #     # AutoTest(number, mac, name, '_P_ttk_hospitals') # -- Кептив на самсунге не всплывает
    #     # AutoTest(number, mac, name, '_P_dit_mts_vdnh')


    def startTestsXiaomiRedmi(number, mac, name):
        AutoTest(number, mac, name, '_P_metro')
        AutoTest(number, mac, name, '_P_cppk')
        AutoTest(number, mac, name, '_P_MCC_incarnet')
        AutoTest(number, mac, name, '_P_aeroexpress')
        AutoTest(number, mac, name, '_p_mvf_bus')
        # AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
        # ЕОС
        AutoTest(number, mac, name, '_P_dit_enforta_street')
        AutoTest(number, mac, name, '_P_dit_akado')
        AutoTest(number, mac, name, '_P_dit_guest_wifi')
        # AutoTest(number, mac, name, '_P_dit_Nauka 3')
        # AutoTest(number, mac, name, '_P_dit_snb')
        # AutoTest(number, mac, name, '_P_dit_almatel')
        # AutoTest(number, mac, name, '_P_dit_beeline')
        AutoTest(number, mac, name, '_P_ttk_hospitals')
        # AutoTest(number, mac, name, '_P_dit_mts_vdnh')
    #
    # def startTestsXiaomiMi(number, mac, name):
    #     AutoTest(number, mac, name, '_P_metro')
    #     AutoTest(number, mac, name, '_P_cppk')
    #     AutoTest(number, mac, name, '_P_MCC_incarnet')
    #     AutoTest(number, mac, name, '_P_aeroexpress')
    #     AutoTest(number, mac, name, '_p_mvf_bus')
    #     AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
    #     # ЕОС
    #     AutoTest(number, mac, name, '_P_dit_enforta_street')
    #     AutoTest(number, mac, name, '_P_dit_akado')
    #     AutoTest(number, mac, name, '_P_dit_guest_wifi')
    #     AutoTest(number, mac, name, '_P_dit_Nauka 3')
    #     AutoTest(number, mac, name, '_P_dit_snb')
    #     AutoTest(number, mac, name, '_P_dit_almatel')
    #     AutoTest(number, mac, name, '_P_dit_beeline')
    #     AutoTest(number, mac, name, '_P_ttk_hospitals')
    #     AutoTest(number, mac, name, '_P_dit_mts_vdnh')
    #
    def startTestsSamsung(number, mac, name):
        # AutoTest(number, mac, name, 'MT_FREE')
        # AutoTest(number, mac, name, '_P_cppk')  # -- Кептив на самсунге не всплывает
        # AutoTest(number, mac, name, '_P_MCC_incarnet')  # -- Кептив на самсунге не всплывает
        # AutoTest(number, mac, name, '_P_aeroexpress')  # -- Кептив на самсунге не всплывает
        # AutoTest(number, mac, name, '_p_mvf_bus')
        # AutoTest(number, mac, name, '_P_Sola_Metrotelecom Free')
        # ЕОС
        # AutoTest(number, mac, name, '_P_dit_enforta_street')
        # AutoTest(number, mac, name, '_P_dit_akado')
        # AutoTest(number, mac, name, '_P_dit_guest_wifi')
        # AutoTest(number, mac, name, '_P_dit_Nauka 3')
        # AutoTest(number, mac, name, '_P_dit_snb')
        # AutoTest(number, mac, name, '_P_dit_almatel')
        AutoTest(number, mac, name, '_P_dit_beeline')
        # AutoTest(number, mac, name, '_P_ttk_hospitals') # -- Кептив на самсунге не всплывает
        # AutoTest(number, mac, name, '_P_dit_mts_vdnh')

    # d(text="Ошибка #900") - внедрить ( появилась после рекламы на мцк)

    startTestsSamsung(number3, MAC3, Name3)
    startTestsXiaomiRedmi(number2, MAC2, Name2)
    # startTestsXiaomiMi(number1, MAC1, Name1)

    SendMessage(f"✅Автотесты завершены📴")  # Отправка сообщения в телеграмм канал
    Send_File("logs/buttonClick.txt")
    print(f"{NowDate()}  📣 :  Автотесты завершены📱")

    # while True:
    #     schedule.run_pending()
    #     sleep(1)
