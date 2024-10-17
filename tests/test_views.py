import json

import pytest
import src.views
from tests import data_for_test
from unittest.mock import patch
from unittest.mock import Mock
import pandas as pd
#with open('data_for_test.py', 'r', encoding='utf-8') as file:
#    list_data_for_test = file.readlines()


@pytest.fixture
def transactions() -> list:  # Имя фикстуры — любое
    return data_for_test.transactions()

@pytest.fixture
def by_category_1() -> list:  # Имя фикстуры — любое
    return data_for_test.by_category_1()

@pytest.fixture
def by_category_2() -> list:  # Имя фикстуры — любое
    return data_for_test.by_category_2()

def test_transactions_by_category(transactions, by_category_1, by_category_2) -> None:
    result = src.views.transactions_by_category(transactions)
    assert result == by_category_1
    result = src.views.transactions_by_category(transactions,False)
    assert result == by_category_2

def test_transactions_to_cash(transactions) -> None:
    result = src.views.transactions_to_cash(transactions)
    assert  result == [('transfer', -83571.01), ('cash', -3000.0)]

def test_total_expenses(transactions) -> None:
    result = src.views.transactions_by_category(transactions, False)

def test_total_receipt(transactions) -> None:
    result = src.views.total_expenses(transactions)
    assert result == -228560.28

@patch('requests.get')
def test_exchange_rate(mock_get) -> None:
    mock_get.return_value.json.return_value = data_for_test.mokc_1()
    mock_get.return_value.status_code = 200
    result = src.views.exchange_rate()
    assert result == {'USD': 97.26, 'EUR': 106.08}


@patch('requests.get')
def test_share_price(mock_get) -> None:
    mock_get.return_value.json.return_value = data_for_test.mock_2()
    result = src.views.share_price()
    assert result == {'AAPL': 229.04, 'AMZN': 186.65, 'GOOGL': 162.08, 'TSLA': 238.77}




# data in the form of list of tuples
data = [("15.09.2021 18:58:43","17.09.2021","*7197","OK","-25100","RUB"
         ,-25100,"RUB",50,"Пополнения",None,"Пятёрочка",
        "0","0","25100")
        ]

# create DataFrame using data
data_xls = pd.DataFrame(data, columns =["Дата операции", "Дата платежа", "Номер карты",
                             "Статус","Сумма операции","Валюта операции","Сумма платежа",
                             "Валюта платежа", "Кэшбэк", "Категория", "MCC",
                             "Описание", "Бонусы (включая кэшбэк)","Округление на инвесткопилку",
                             "Сумма операции с округлением"])



#@patch('src.views.read_xls')
def test_events() -> None:
    mock_random = Mock(return_value=data_xls)
    pd.read_excel = mock_random

    mock_random_2 = Mock(return_value={'AAPL': 229.04, 'AMZN': 186.65, 'GOOGL': 162.08, 'TSLA': 238.77})
    src.views.share_price = mock_random_2

    #status, result = read_xls("my_file.xls")

    #mock_get.return_value = x
    result = src.views.events('16.09.2021')

    assert  result ==  json.dumps (data_for_test.event_json(), indent=4, ensure_ascii=False)



