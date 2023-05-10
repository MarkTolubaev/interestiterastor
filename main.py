from decimal import Decimal

from pandas import set_option

from Interests.InterestIterator import InterestIterator
from Utils.data_frames import create_interest_df
from Utils.dimensions import Ruble, Date


def test_iterator():
    # тестовые данные из ТЗ для задания 1
    deposit = {
        3: Ruble(100),
        4: Ruble(0),
        5: Ruble(0)
    }

    max_withdraw = {
        3: Ruble(40),
        4: Ruble(40),
        5: Ruble(40)
    }

    rate = Decimal('0.1')

    dates = {
        3: Date(2023, 1, 10),
        4: Date(2023, 2, 10),
        5: Date(2023, 3, 10)
    }

    # Заголовки для формирования таблицы в консоле
    headers = ['period', 'date1', 'date2', 'deposit', 'max_withdraw', 'rate']
    header_string = f"{headers[0]:<8}" \
                    f"{headers[1]:12}" \
                    f"{headers[2]:12}" \
                    f"{headers[3]:<8}" \
                    f"{headers[4]:<14}" \
                    f"{headers[5]:<10}"

    print(header_string)

    # фрагмент скрипта из ТЗ
    interest_iter = InterestIterator(deposit, max_withdraw, rate, dates)

    for row in interest_iter:
        print(row)

    print()  # перенос строки


def test_data_frame():
    # тестовые данные из ТЗ для задания 2
    deposit = {
        1: Ruble(100),
        2: Ruble(0),
        3: Ruble(0),
        4: Ruble(0)
    }

    max_withdraw = {
        1: Ruble(40),
        2: Ruble(40),
        3: Ruble(40),
        4: Ruble(0)
    }

    rate = Decimal('0.1')

    dates = {
        1: Date(2023, 1, 10),
        2: Date(2023, 2, 10),
        3: Date(2023, 3, 10),
        4: Date(2023, 4, 10)
    }

    df = create_interest_df(deposit, max_withdraw, rate, dates)
    # только для отладки
    set_option('display.max_columns', None)
    set_option('display.width', 100)
    print(df)


if __name__ == '__main__':
    test_iterator()
    test_data_frame()
