import schedule
from Functions.TelegramApi import SendMessage
from SIMF_API import SIMF_STEND
from Functions.DataName import NowDate
from time import sleep
from schedule import every, repeat
from Functions import Schet

if __name__ == "__main__":
    Schet.init()
    print(f"{NowDate()}  📣 :  Автотесты запущены📱")
    print(f"_____________________________________________________________")
    with open("buttonClick.txt", 'w', encoding='utf-8') as f:
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


    @repeat(every(30).seconds, number2, MAC2, Name2)
    def startTestsXiaomiRedmi (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name, "_P_AP_TEST105")


    def startTestsXiaomiMi (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name, "_P_AP_TEST105")


    def startTestsSamsung (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name, "_P_AP_TEST105")


    startTestsXiaomiRedmi(number2, MAC2, Name2)


    while True:
        schedule.run_pending()
        sleep(1)
