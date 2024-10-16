import pytest
import src.views
from tests import data_for_test
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

def transactions_to_cash() -> None:
    result = src.views.transactions_to_cash(transactions)


def total_expenses() -> None:
    result = src.views.transactions_by_category(transactions, False)

def total_receipt() -> None:
    result = src.views.total_expenses(transactions)


def exchange_rate() -> None:
    result = src.views.exchange_rate()


def share_price() -> None:
    result = src.views.share_price()

