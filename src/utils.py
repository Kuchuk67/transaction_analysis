import os
from config import PATH_HOME
import pandas as pd
from typing import Iterable
from dateutil.relativedelta import relativedelta
import datetime

def read_xls(file_name: str) -> (str, Iterable):
    '''
    Читает файл xlsx c транзакциями,
    - Отдает только статус == 'OK'
    - Замена NAN на пробелы
    - Переименовывает столбцы на английский
    - Проверяет наличие нужных колонок
    -
    Пример:
    status,x = read_xls('operations.xlsx')
    :param file_name:
    :return: status: Ok при успехе или описание ошибки
    DataFrame: с данными или None
    '''
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    try:
        excel_data = pd.read_excel(path_to_file)
    except FileNotFoundError:
        status = "FileNotFoundError"
        return status, None
    except Exception:
        status = "Error Type xls"
        return status, None

    excel_data = excel_data.fillna('')
    dict_translation_head = {"Дата операции": "transaction_date",
                             "Дата платежа": "payment_date",
                             "Номер карты": "card_number",
                             "Статус": "status",
                             "Сумма операции": "amount",
                             "Валюта операции": "currency",
                             "Сумма платежа": "payment_amount",
                             "Валюта платежа": "payment_currency",
                             "Кэшбэк": "cashback",
                             "Категория": "category",
                             "MCC": "mcc",
                             "Описание": "description",
                             "Бонусы (включая кэшбэк)": "bonuses",
                             "Округление на инвесткопилку": "investment_piggy",
                             "Сумма операции с округлением": "amount_with_rounding",
                             }

    excel_data.rename(columns=dict_translation_head, inplace=True)

    print(excel_data)
    # проверка наличия нужных колонок
    important_columns = ["transaction_date", "status", "amount"]
    if set(important_columns).issubset(excel_data.columns):
        status = 'Ok'
        #excel_data
        dict_data = excel_data.loc[ excel_data.status == 'OK' ].to_dict(orient="records")

    else:
        status = 'not important columns'
        dict_data = None

    return status, dict_data




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

#data_start, data_end =(financial_period('12.10.2024', 'N'))
#print(data_start, data_end)

def data_formater(date_trans: str) -> str:
    return f'{date_trans[6:10]}.{date_trans[3:5]}.{date_trans[0:2]}'

def filter_transaction(transactions: list, data_start: str, data_end: str) -> list:
    '''
    Возращает новый список словарей транзакций отфильтрованных по датам
    :param transactions:  список со словарями транзакций
    :param data_start:   дата начала выборки 01.01.2022
    :param data_end:    дата конца выборки  31.12.2022
    :return: список со словарями транзакций указанного периода
    '''

    transactions_filter_data = []
    data_start = data_formater(data_start)

    data_end = data_formater(data_end)

    for transaction in transactions:
        data_transaction = data_formater( transaction.get('transaction_date'))

        if  data_transaction < data_start:
            break

        if data_start <= data_transaction <= data_end:
            transactions_filter_data.append(transaction)


    return transactions_filter_data


status,x = read_xls('operations.xlsx')
#print(x[0])
q = filter_transaction(x,'14.11.2021','14.11.2021')
print(*q, sep='\n')
