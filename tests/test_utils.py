from src.utils import read_xls, financial_period, filter_transaction, workday_or_weekday
import pandas as pd
from unittest.mock import Mock
from freezegun import freeze_time
import pytest

# data in the form of list of tuples
data = [("15.09.2021 18:58:43","17.09.2021","*7197","OK","-25100","RUB"
         ,"-25100","RUB",None,"Пополнения",None,"Пятёрочка",
        "0","0","25100")
        ]

# create DataFrame using data
data_xls = pd.DataFrame(data, columns =["Дата операции", "Дата платежа", "Номер карты",
                             "Статус","Сумма операции","Валюта операции","Сумма платежа",
                             "Валюта платежа", "Кэшбэк", "Категория", "MCC",
                             "Описание", "Бонусы (включая кэшбэк)","Округление на инвесткопилку",
                             "Сумма операции с округлением"])



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

data_dict = [{'transaction_date': '15.09.2021 18:58:43',
              'payment_date': '17.09.2021',
              'card_number': '*7197',
              'status': 'OK',
              'amount': '-25100',
              'currency': 'RUB',
              'payment_amount': '-25100',
              'payment_currency': 'RUB',
              'cashback': '',
              'category': 'Пополнения',
              'mcc': '',
              'description': 'Пятёрочка',
              'bonuses': '0',
              'investment_piggy': '0',
              'amount_with_rounding': '25100'}
             ]

def test_read_xls() -> None:
    mock_random = Mock(return_value=data_xls)
    pd.read_excel = mock_random
    status,result = read_xls("my_file.xls")
    assert status == 'Ok'
    #assert result.equals(data_xls_result)
    assert  result == data_dict




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


data_financial_period = [{'transaction_date': '15.10.2022 18:58:43'},
 {'transaction_date': '14.01.2022 18:58:43'},
 {'transaction_date': '01.12.2024 18:58:43'},
 {'transaction_date': '28.09.2021 18:58:43'},
 ]

result_financial_period = [{'transaction_date': '15.10.2022 18:58:43'},
 {'transaction_date': '14.01.2022 18:58:43'}, ]


def test_filter_transaction() -> None:
    result = filter_transaction(data_financial_period, '01.01.2022', '01.12.2022')
    assert result == result_financial_period


def test_workday_or_weekday() -> None:
    assert workday_or_weekday('15.10.2024')
    assert workday_or_weekday('16.10.2024')
    assert workday_or_weekday('17.10.2024')
    assert workday_or_weekday('18.10.2024')
    assert not workday_or_weekday('19.10.2024')
    assert not workday_or_weekday('20.10.2024')
    assert workday_or_weekday('21.10.2024')