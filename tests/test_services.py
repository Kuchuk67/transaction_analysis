from src.services import increased_cashback
from tests import data_for_test
import pytest
import json


@pytest.fixture
def transactions() -> list:  # Имя фикстуры — любое
    return data_for_test.transactions()


def test_increased_cashback(transactions) -> None:
    result = increased_cashback(transactions, '2021', '11')
    assert result == json.dumps({"Супермаркеты": 78.0, "Косметика": 11.0, "Фастфуд": 1.0}, indent=4, ensure_ascii=False)
    result = increased_cashback(transactions, '2023', '01')
    assert result == json.dumps({}, indent=4, ensure_ascii=False)
