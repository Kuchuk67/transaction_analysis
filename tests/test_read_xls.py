from src.read_xls import read_xls
import pandas as pd
from unittest.mock import Mock

data_xls = pd.DataFrame(
    {
        "Дата операции": ["15.09.2021 18:58:43"],
                             "Дата платежа": ["17.09.2021"],
                             "Номер карты": ["*7197"],
                             "Статус": ["OK"],
                             "Сумма операции": ["-25100"],
                             "Валюта операции": ["RUB"],
                             "Сумма платежа": ["-25100"],
                             "Валюта платежа": ["RUB"],
                             "Кэшбэк": [None],
                             "Категория": ["Пополнения"],
                             "MCC": [None],
                             "Описание": ["Пятёрочка"],
                             "Бонусы (включая кэшбэк)": ["0"],
                             "Округление на инвесткопилку": ["0"],
                             "Сумма операции с округлением": ["25100"],
    },
)

data_xls_result = pd.DataFrame(
    {
        "transaction_date": ["15.09.2021 18:58:43"],
                             "payment_date": ["17.09.2021"],
                             "card_number": ["*7197"],
                             "status": ["OK"],
                             "amount": ["-25100"],
                             "currency": ["RUB"],
                             "payment_amount": ["-25100"],
                             "payment_currency": ["RUB"],
                             "cashback": [""],
                             "category": ["Пополнения"],
                             "mcc": [""],
                             "description": ["Пятёрочка"],
                             "bonuses": ["0"],
                             "investment_piggy": ["0"],
                             "amount_with_rounding": ["25100"],
    },
)



def test_read_xls() -> None:
    mock_random = Mock(return_value=data_xls)
    pd.read_excel = mock_random
    status,result = read_xls("my_file.xls")
    assert status == 'Ok'
    assert result.equals(data_xls_result)
