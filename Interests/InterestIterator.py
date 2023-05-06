from Interests.Interest import InterestInput
from decimal import Decimal
from datetime import date, datetime


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
        self.__pointer = next(iter(self.__withdraw.keys()))

    def __next__(self) -> InterestInput:
        if self.__pointer not in self.__withdraw:
            self.__pointer = next(iter(self.__withdraw.keys()))
            raise StopIteration

        res = InterestInput(self.__pointer,
                            self.__dates[self.__pointer],
                            self.__dates[self.__pointer + 1 if self.__pointer + 1 in self.__dates else self.__pointer],
                            self.__withdraw[self.__pointer],
                            self.__max_return[self.__pointer],
                            self.__rate)
        self.__pointer += 1

        return res

    def __iter__(self):
        return self


if __name__ == '__main__':
    t1 = datetime.now().microsecond
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

    print((datetime.now().microsecond - t1))
