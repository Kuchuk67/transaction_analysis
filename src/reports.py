import pandas as pd
from typing import Optional
from src.utils import read_xls,financial_period,filter_transaction,workday_or_weekday

def spending_by_workday(transactions: pd.DataFrame,
                        date: Optional[str] = None) -> pd.DataFrame:
    data_start, data_end = financial_period(date,'3M')


    #transactions = transactions.to_dict(orient="records")

    #transactions = filter_transaction(transactions,data_start, data_end)

    #transactions_work = transactions.loc[ workday_or_weekday(transactions.payment_date) == False ]
    # добавим новый столбец True 'workday' - рабочий день
    transactions['workday'] = transactions.payment_date.map(workday_or_weekday)

    transactions_work = transactions.loc[transactions.payment_date if workday_or_weekday(transactions.payment_date) == True else  1]

    print(transactions)

ststus, df = read_xls('operations.xlsx', df = True)
spending_by_workday(df, date='04.11.2021')



