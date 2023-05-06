from datetime import date
from decimal import Decimal

from Interests.descriptors import ReadOnlyDescriptor


class InterestInput:
    period = ReadOnlyDescriptor()
    date1 = ReadOnlyDescriptor()
    date2 = ReadOnlyDescriptor()
    withdraw = ReadOnlyDescriptor()
    max_return = ReadOnlyDescriptor()
    rate = ReadOnlyDescriptor()

    def __init__(self,
                 period: int,
                 date1: date,
                 date2: date,
                 withdraw: Decimal,
                 max_return: Decimal,
                 rate: Decimal):
        """
        Класс представляющий собой сведенья об интересе лизингодателя

        :param period: номер периода
        :param date1: дата начала периода
        :param date2: дата ĸонца периода
        :param withdraw: сумма, ĸоторую получает ĸлиент по ĸредиту в данном периоде
        :param max_return: маĸсимальная сумма, ĸоторую ĸлиент может вернуть в данном периоде
        :param rate: Ставĸа ĸредита
        """

        self.period = period
        self.date1 = date1
        self.date2 = date2
        self.withdraw = withdraw
        self.max_return = max_return
        self.rate = rate

    def __str__(self):
        return f"{self.period:<8}" \
               f"{self.date1.strftime('%Y-%m-%d'):12}" \
               f"{self.date2.strftime('%Y-%m-%d'):12}" \
               f"{self.withdraw:<14.2f}" \
               f"{self.max_return:<14.2f}" \
               f"{self.rate:<5.2f}\n{'-'*65}"


if __name__ == '__main__':
    headers = ('period', 'date1', 'date2', 'deposit', 'max_withdraw', 'rate')
    header_string = f"{headers[0]:<8}" \
                    f"{headers[1]:12}" \
                    f"{headers[2]:12}" \
                    f"{headers[3]:<14}" \
                    f"{headers[4]:<14}" \
                    f"{headers[5]:<5}" \
                    f"\n{'-'*65}"

    obj1 = InterestInput(1, date(2023, 5, 6), date(2023, 5, 7), Decimal(100), Decimal(40), Decimal(0.1))
    obj2 = InterestInput(2, date(2023, 5, 7), date(2023, 5, 8), Decimal(0), Decimal(40), Decimal(0.1))
    obj3 = InterestInput(3, date(2023, 5, 8), date(2023, 5, 9), Decimal(0), Decimal(40), Decimal(0.1))

    print(header_string)
    print(obj1)
    print(obj2)
    print(obj3)

    try:
        del obj2.period
    except AttributeError as e:
        print(e)

    try:
        obj2.period = 10
    except AttributeError as e:
        print(e)
