from Interests.Interest import InterestInput
from decimal import Decimal
from datetime import date


class InterestIterator:
    def __init__(self,
                 deposit: dict[int, Decimal],
                 max_withdraw: dict[int, Decimal],
                 rate: Decimal,
                 dates: dict[int, date]):
        """
        Класс представляющий собой итератор периодов с информацией об интересе лизингодателя

        :param deposit: суммы, ĸоторые получает ĸлиент по ĸредиту в соответствующем периоде
        :param max_withdraw: максимальная сумма, ĸоторую ĸлиент может вернуть в соответствующем периоде
        :param rate: ставĸа ĸредита
        :param dates: даты платежей по ĸредиту
        """

        self.__withdraw = deposit
        self.__max_return = max_withdraw
        self.__rate = rate
        self.__dates = dates
        self.__cursor = None

    def __next__(self) -> InterestInput:
        cursor, date1, date2 = next(self.__cursor)
        res = InterestInput(cursor,
                            date1,
                            date2,
                            self.__withdraw[cursor].quantize(Decimal('0.01')),
                            self.__max_return[cursor].quantize(Decimal('0.01')),
                            self.__rate.quantize(Decimal('0.01')))
        return res

    def __iter__(self):
        self.__cursor = self.__create_cursor()
        return self

    def __create_cursor(self):
        step = next(iterator := iter(self.__dates))
        while True:
            next_step = next(iterator, step)
            yield step, self.__dates[step], self.__dates[next_step]
            if next_step == step:
                break
            step = next_step
