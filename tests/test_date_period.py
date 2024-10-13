from src.date_period import financial_period
from freezegun import freeze_time


@freeze_time("Jan 14th, 2012")
def test_financial_period_freez():
    assert financial_period() == ('01.01.2012', '14.01.2012')


def test_financial_period() -> None:
    result = financial_period('12.10.2024', 'W')
    assert result == ('07.10.2024', '12.10.2024')
    result = financial_period('29.02.2024', 'y')
    assert result == ('28.02.2023', '29.02.2024')
    result = financial_period('29.02.2024', '3m')
    assert result == ('29.11.2023', '29.02.2024')
    result = financial_period('29.02.2024', 'all')
    assert result == ('01.01.1900', '29.02.2024')


