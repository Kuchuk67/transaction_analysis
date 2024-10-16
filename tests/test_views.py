import pytest
import src.views
from tests import data_for_test
from unittest.mock import patch
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

def total_expenses(transactions) -> None:
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

