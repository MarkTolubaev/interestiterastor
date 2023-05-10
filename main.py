from decimal import Decimal

from pandas import DataFrame, set_option

from Interests.InterestIterator import InterestIterator
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


def create_df(withdraw, max_return, credit_rate, credit_dates):
    interest_iter = InterestIterator(withdraw, max_return, credit_rate, credit_dates)

    balance = None
    df_date = {}

    for row in interest_iter:
        if not balance:
            balance = row.withdraw

        interest = (balance * row.rate * (row.date2 - row.date1).days / 365).quantize(Decimal('0.01'))
        payment = row.max_return if row.max_return < balance + interest else balance + interest

        df_date[row.period] = [row.period,
                               row.date1,
                               row.date2,
                               row.withdraw,
                               row.max_return,
                               row.rate,
                               balance,
                               interest,
                               payment]

        balance = balance - payment + interest

    data_frame = DataFrame.from_dict(df_date,
                                     orient='index',
                                     columns=['period',
                                              'date1',
                                              'date2',
                                              'deposit',
                                              'max_withdraw',
                                              'rate',
                                              'balance',
                                              'interest',
                                              'payment'])

    return data_frame


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

    df = create_df(deposit, max_withdraw, rate, dates)
    # только для отладки
    set_option('display.max_columns', None)
    set_option('display.width', 100)
    print(df)


if __name__ == '__main__':
    test_iterator()
    test_data_frame()
