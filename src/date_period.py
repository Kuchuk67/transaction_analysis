from time import strftime
from dateutil.relativedelta import relativedelta
import datetime

def financial_period(data_end: str ='' , period: str='M' ) -> tuple[str, str,]:
    '''
    функция вывода  диапазона дат в формате 31.12.2021
    :param data_end: конец диапазона (31.12.2021)  по умолчанию текущая дата
    period: размер  диапазона: W — неделя, на которую приходится дата;
    M (по умолчанию) — месяц, на который приходится дата;
    3M - три месяца от переданной даты:
    Y — год, на который приходится дата;
    ALL — все данные,
    :return:
    data_start
    data_end
    '''

    try:
        data_end_iso = datetime.datetime.strptime(data_end, "%d.%m.%Y")
    except ValueError:
        data_end_iso = datetime.datetime.now()

    period = period.upper()
    # текущая неделя
    if period == 'W':
        day_delta = datetime.datetime.weekday(data_end_iso)
        data_start_iso = data_end_iso - datetime.timedelta(days=day_delta)

    elif period == '3M':
        data_start_iso = data_end_iso - relativedelta(months=+3)

    elif period == 'Y':
        data_start_iso = data_end_iso - relativedelta(years=+1)

    elif  period == 'ALL':
        data_start_iso = datetime.datetime(1900, 1, 1, 0, 0, 0)

    else:
        day_delta = data_end_iso.day
        data_start_iso = data_end_iso - datetime.timedelta(days=day_delta - 1)

    data_end = datetime.datetime.strftime(data_end_iso,"%d.%m.%Y")
    data_start = datetime.datetime.strftime(data_start_iso, "%d.%m.%Y")
    return data_start, data_end

data_start, data_end =(financial_period('12.10.2024', 'N'))
print(data_start, data_end)

