import random
import datetime

class Time_work:

    def __init__(self, path, method):
        self.path = path
        self.method = method

    def __enter__(self):
        self.file = open(self.path, self.method, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self.method == 'w':
            now = datetime.datetime.now()
            self.file.write(f'\n Начало выполнения кода {now}\n')

            end = datetime.datetime.today()
            self.file.write(f'\n Конец выполнения кода {end}\n')
            delta = end - now
            self.file.write(f'Время выпонения кода {delta}\n')
            if exc_type:
                self.file.write(f'{exc_val}\n')
                self.file.write(f'{exc_tb.tb_frame}')
        self.file.close()

def zodiac(month, day):

    if (month.lower() == 'декабрь' and day <=31 and day >= 22)  or (month.lower() == 'январь' and day <=20 and day >= 1):
      your_result =  'Козерог'

    if (month.lower() == 'январь' and day <=31 and day >= 21)  or (month.lower() == 'февраль' and day <=19 and day >= 1):
      your_result =  'Водолей'

    if (month.lower() == 'февраль' and day <=29 and day >= 20)  or (month.lower() == 'март' and day <=20 and day >= 1):
      your_result =  'Рыбы'

    if (month.lower() == 'март' and day <=30 and day >= 21)  or (month.lower() == 'апрель' and day <=20 and day >= 1):
      your_result =  'Овен'

    if (month.lower() == 'апрель' and day <=30 and day >= 21)  or (month.lower() == 'май' and day <=21 and day >= 1):
      your_result =  'Телец'

    if (month.lower() == 'май' and day <=31 and day >= 22)  or (month.lower() == 'июнь' and day <=21 and day >= 1):
      your_result =  'Близнецы'

    if (month.lower() == 'июнь' and day <=30 and day >= 22)  or (month.lower() == 'июль' and day <=23 and day >= 1):
      your_result =  'Рак'

    if (month.lower() == 'июль' and day <=31 and day >= 24)  or (month.lower() == 'август' and day <=23 and day >= 1):
      your_result =  'Лев'

    if (month.lower() == 'август' and day <=31 and day >= 24)  or (month.lower() == 'сентябрь' and day <=23 and day >= 1):
      your_result =  'Дева'

    if (month.lower() == 'сентябрь' and day <=30 and day >= 24)  or (month.lower() == 'октябрь' and day <=23 and day >= 1):
      your_result =  'Весы'

    if (month.lower() == 'октябрь' and day <=31 and day >= 24)  or (month.lower() == 'ноябрь' and day <=22 and day >= 1):
      your_result =  'Скорпион'

    if (month.lower() == 'ноябрь' and day <=31 and day >= 23)  or (month.lower() == 'декабрь' and day <=21 and day >= 1):
      your_result =  'Стрелец'
    return your_result

if __name__ == '__main__':
    with Time_work('test.txt', 'w') as test_file:
        month = ['январь', 'февраль', 'март', 'апрель', 'май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
        day = range(1, 28)
        for i in range(10):
            random_month = random.choice(month)
            random_day = random.choice(day)
            result = zodiac(random_month, random_day)
            test_file.write(f'Вы ввели: {random_month} {random_day}. Ваш знак зодиака: {result}\n')






