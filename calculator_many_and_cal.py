# Калькулятор денег должен уметь:
#
# Сохранять новую запись о расходах методом add_record()+
# Считать, сколько денег потрачено сегодня методом get_today_stats()+
# Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или
# евро — метод get_today_cash_remained(currency)+
# Считать, сколько денег потрачено за последние 7 дней — метод get_week_stats()
#
# Калькулятор калорий должен уметь:
#
# Сохранять новую запись о приёме пищи— метод add_record()
# Считать, сколько калорий уже съедено сегодня — метод get_today_stats()
# Определять, сколько ещё калорий можно/нужно получить сегодня — метод
# get_calories_remained()
# Считать, сколько калорий получено за последние 7
# дней — метод get_week_stats()

import datetime as dt


class Record:

    def __init__(self, amount, comment, date_add=dt.date.today()):
        self.amount = amount
        self.comment = comment
        if isinstance(date_add, str):
            self.date_add = dt.datetime.strptime(date_add, '%d.%m.%Y').date()
        else:
            self.date_add = date_add


class Calculator:

    def __init__(self, limit, list_history=[], day_sum=0, remains=0,
                 week_sum=0):
        self.list_history = list_history
        self.day_sum = day_sum
        self.limit = limit
        self.remains = remains
        self.week_sum = week_sum

    # Добавить запись
    def add_record(self, data: Record):
        self.list_history.append(data)

    # Сумма за день
    def get_today_stats(self):
        for i in range(len(self.list_history)):
            if self.list_history[i].date_add == dt.date.today():
                self.day_sum += self.list_history[i].amount
        print(self.day_sum)

    # Сумма за неделю
    def get_week_stats(self):
        for i in range(len(self.list_history)):
            if (self.list_history[i].date_add +
                    + dt.timedelta(7)) >= dt.date.today():
                self.week_sum += self.list_history[i].amount
        print(self.week_sum)


class CaloriesCalculator(Calculator):

    # Дневной остаток
    def get_today_cash_remained(self):
        self.remains = self.limit - self.day_sum
        if self.limit == 0:
            print('Дневной лимит каллорий не задан')
        elif self.remains > 0:
            print(f'Ещё можно съесть на {self.remains}'
                  ' калорий')
        elif self.remains == 0:
            print('Лимит исчерпан, больше есть нельзя')
        else:
            print(f'Переизбыток в {self.remains*(-1)}'
                  ' калорий, пора худеть')


class MoneyCalculator(Calculator):

    # Дневной остаток
    def get_today_cash_remained(self, wallet: str):
        self.remains = self.limit - self.day_sum
        if wallet == 'usd':
            self.remains = int(self.remains/56)
        elif wallet == 'eur':
            self.remains = int(self.remains/57)
        if self.limit == 0:
            print('Лимит не задан')
        elif self.remains > 0:
            print(f'Ещё есть запас в {self.remains}'
                  f' {wallet}')
        elif self.remains == 0:
            print('Запас исчерпан')
        else:
            print(f'Недостаток {self.remains*(-1)}'
                  f' {wallet}')


if __name__ == '__main__':

    meal_one = Record(3255, 'Йогурт.', '12.07.2022')
    meal_two = Record(2, 'Сок.', '12.07.2022')
    meal_three = Record(3353, 'Мясо', '18.07.2022')
    purchase_one = Record(100, 'Кофе', '18.07.2022')
    purchase_two = Record(300, 'Тренажёрка', '18.07.2022')
    purchase_three = Record(600, 'Проезд', '12.07.2022')

    cal = CaloriesCalculator(5000, [])
    cal.add_record(meal_one)
    cal.add_record(meal_two)
    cal.add_record(meal_three)

    money = MoneyCalculator(1000, [])
    money.add_record(purchase_one)
    money.add_record(purchase_two)
    money.add_record(purchase_three)

    cal.get_today_stats()
    cal.get_week_stats()
    cal.get_today_cash_remained()

    money.get_today_stats()
    money.get_week_stats()
    money.get_today_cash_remained('eur')
