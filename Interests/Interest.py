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
        Класс представляющий собой сведенья о  параметрах кредита за один период

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
               f"{self.withdraw:<8.2f}" \
               f"{self.max_return:<14.2f}" \
               f"{self.rate:<10.2f}"
