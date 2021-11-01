from Functions.TelegramApi import Send_File
from Functions.TelegramApi import SendMessage
from Functions.DataName import NowDate

from Tests import EOS
from Tests import Sbornay
from Tests import Sola
from Tests import metro

if __name__ == "__main__":
    print(f"{NowDate()}  📣 :  Автотесты запущены📱")
    print(f"_____________________________________________________________")
    with open("logs/buttonClick.txt", 'w', encoding='utf-8') as f:
        f.write(f"{NowDate()}  📣 :  Автотесты запущены🚀\n")
        f.write(f"_____________________________________________________________\n")

    # f = open("logs/buttonClick2.txt", 'w', encoding='utf-8')

    # XiaomiMi9
    # startTests(number1, MAC1, Name1)
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


    # @repeat(every(4).minutes, number2, MAC2, Name2)
    # @repeat(every(10).minutes, number1, MAC1, Name1)
    # @repeat(every(4).minutes, number3, MAC3, Name3)


    def startTestsXiaomiRedmi (number, mac, name):
        # metro_Home.AvtoTest(number, mac, name)
        # metro.AvtoTest(number, mac, name)
        # cppk.AvtoTest(number, mac, name)
        # MCC.AvtoTest(number, mac, name)
        # aeroexpress.AvtoTest(number, mac, name)
        # Sola.AvtoTest(number, mac, name)
        # SIMF_STEND.AvtoTest(number, mac, name)

        # EOS.AvtoTest(number, mac, name, '_P_dit_enforta_street')
        # EOS.AvtoTest(number, mac, name, '_P_dit_akado')
        # EOS.AvtoTest(number, mac, name, '_P_dit_guest_wifi')
        # EOS.AvtoTest(number, mac, name, '_P_dit_Nauka 3')
        # EOS.AvtoTest(number, mac, name, '_P_dit_snb')
        # EOS.AvtoTest(number, mac, name, '_P_dit_almatel')
        # EOS.AvtoTest(number, mac, name, '_P_dit_beeline')
        EOS.AvtoTest(number, mac, name, '_P_dit_mts_vdnh')


    def startTestsXiaomiMi (number, mac, name):

        Sbornay.AvtoTest(number, mac, name, '_P_MCC_incarnet')
        Sbornay.AvtoTest(number, mac, name, '_P_aeroexpress')
        Sbornay.AvtoTest(number, mac, name, '_P_cppk')


        # EOS.AvtoTest(number, mac, name, '_P_dit_enforta_street')
        # EOS.AvtoTest(number, mac, name, '_P_dit_akado')
        # EOS.AvtoTest(number, mac, name, '_P_dit_guest_wifi')
        # EOS.AvtoTest(number, mac, name, '_P_dit_Nauka 3')
        # EOS.AvtoTest(number, mac, name, '_P_dit_snb')
        # EOS.AvtoTest(number, mac, name, '_P_dit_almatel')
        # EOS.AvtoTest(number, mac, name, '_P_dit_beeline')
        # EOS.AvtoTest(number, mac, name, '_P_dit_mts_vdnh')


    def startTestsSamsung (number, mac, name):
        # metro_Home.AvtoTestMetro(number, mac, name)
        # metro.AvtoTestMetro(number, mac, name)
        # cppk.AvtoTestMetro(number, mac, name)
        # MCC.AvtoTestMetro(number, mac, name)
        # aeroexpress.AvtoTest(number, mac, name)
        Sola.AvtoTest(number, mac, name)

        # EOS.AvtoTest(number, mac, name, '_P_dit_enforta_street')
        # EOS.AvtoTest(number, mac, name, '_P_dit_akado')
        # EOS.AvtoTest(number, mac, name, '_P_dit_guest_wifi')
        # EOS.AvtoTest(number, mac, name, '_P_dit_Nauka 3')
        # EOS.AvtoTest(number, mac, name, '_P_dit_snb')
        # EOS.AvtoTest(number, mac, name, '_P_dit_almatel')
        # EOS.AvtoTest(number, mac, name, '_P_dit_beeline')
        EOS.AvtoTest(number, mac, name, '_P_dit_mts_vdnh')


    # d(text="Ошибка #900") - внедрить ( появилась после рекламы на мцк)
    # startTestsSamsung(number3, MAC3, Name3)
    # startTestsXiaomiRedmi(number2, MAC2, Name2)
    startTestsXiaomiMi(number1, MAC1, Name1)

    SendMessage(f"✅Автотесты завершены📴")  # Отправка сообщения в телеграмм канал
    Send_File("logs/buttonClick.txt")
    print(f"{NowDate()}  📣 :  Автотесты завершены📱")

    # schedule.every(4).minutes.do(startTests, number=number2, mac=MAC2, name=Name2)

    #
    # while True:
    #     schedule.run_pending()
    #     sleep(1)
