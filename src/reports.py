import pandas as pd
from typing import Optional
from src.utils import read_xls,financial_period,filter_transaction

def spending_by_workday(transactions: pd.DataFrame,
                        date: Optional[str] = None) -> pd.DataFrame:
    data_start, data_end = financial_period(date,'3M')
    transactions = transactions.to_dict(orient="records")

    transactions = filter_transaction(transactions,data_start, data_end)

    print(transactions)

ststus, df = read_xls('operations.xlsx', df = True)
spending_by_workday(df, date='04.11.2021')



