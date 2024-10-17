import pandas as pd
from typing import Optional
from src.utils import read_xls

def spending_by_workday(transactions: pd.DataFrame,
                        date: Optional[str] = None) -> pd.DataFrame:
    pass


df = read_xls('operations.xlsx', df = True)
print(df)


