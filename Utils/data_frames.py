from decimal import Decimal

from pandas import DataFrame

from Interests.InterestIterator import InterestIterator


def create_interest_df(withdraw, max_return, credit_rate, credit_dates):
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
