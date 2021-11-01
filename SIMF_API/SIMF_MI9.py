import schedule
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



    def startTestsXiaomiRedmi (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name)


    @repeat(every(30).seconds, number1, MAC1, Name1)
    def startTestsXiaomiMi (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name)


    def startTestsSamsung (number, mac, name):
        SIMF_STEND.AvtoTestMetro(number, mac, name)


    startTestsXiaomiMi(number1, MAC1, Name1)
    # schedule.every(4).minutes.do(startTests, number=number2, mac=MAC2, name=Name2)

    while True:
        schedule.run_pending()
        sleep(1)
