from src.utils import read_xls,financial_period
import pandas as pd
from unittest.mock import Mock
from freezegun import freeze_time
import pytest

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





@freeze_time("Jan 14th, 2012")
def test_financial_period_freez():
    assert financial_period() == ('01.01.2012', '14.01.2012')
    assert financial_period('sfgsdf','ddfdf') == ('01.01.2012', '14.01.2012')


@pytest.mark.parametrize(
    "data_start, data_end, period",
    [
        ('07.10.2024', '12.10.2024','W'),
        ('28.02.2023', '29.02.2024','y'),
        ('29.11.2023', '29.02.2024','3m'),
        ('01.01.1900', '29.02.2024','all'),
        ('01.10.2024', '29.10.2024',''),

    ],
)
def test_financial_period(data_start, data_end, period) -> None:
    result = financial_period(data_end, period)
    assert result == (data_start, data_end)




