from src.date_period import financial_period
from freezegun import freeze_time
import pytest


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



