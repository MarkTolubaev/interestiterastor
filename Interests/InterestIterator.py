from Interests.Interest import InterestInput
from decimal import Decimal
from datetime import date, time


class InterestIterator:
    def __init__(self,
                 withdraw: dict[int, Decimal],
                 max_return: dict[int, Decimal],
                 rate: Decimal,
                 dates: dict[int, date]):
        """
        Класс представляющий собой итератор периодов с информацией об интересе лизингодателя

        :param withdraw: суммы, ĸоторые получает ĸлиент по ĸредиту в соответствующем периоде
        :param max_return: максимальная сумма, ĸоторую ĸлиент может вернуть в соответствующем периоде
        :param rate: ставĸа ĸредита
        :param dates: даты платежей по ĸредиту
        """

        self.__withdraw = withdraw
        self.__max_return = max_return
        self.__rate = rate
        self.__dates = dates

        self.__pointer = 0

    def __next__(self) -> InterestInput:
        try:

            k = next(k for k in self.__withdraw.keys() if k > self.__pointer)

        except StopIteration:
            self.__pointer = 0
            raise
        self.__pointer = k
        return InterestInput(k,
                             self.__dates[k],
                             self.__dates[k + 1 if k + 1 in self.__dates else k],
                             self.__withdraw[k],
                             self.__max_return[k],
                             self.__rate)

    def __iter__(self):
        return self


if __name__ == '__main__':

    deposit = {
        3: Decimal(100),
        4: Decimal(0),
        5: Decimal(0)
    }

    max_withdraw = {
        3: Decimal(40),
        4: Decimal(40),
        5: Decimal(40)
    }

    rate = Decimal(0.1)

    dates = {
        3: date(2023, 1, 10),
        4: date(2023, 2, 10),
        5: date(2023, 3, 10)
    }

    interest_iter = InterestIterator(deposit, max_withdraw, rate, dates)

    for row in interest_iter:
        print(row)

    print("and the next time...")

    for row in interest_iter:
        print(row)
