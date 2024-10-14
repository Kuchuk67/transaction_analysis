import os
from config import PATH_HOME
import pandas as pd
from typing import Iterable


def read_xls(file_name: str) -> (str, Iterable):
    '''
    Читает файл xlsx c транзакциями,
    - Замена NAN на пробелы
    - Переименовывает столбцы на английский
    - Проверяет наличие нужных колонок
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
    # проверка наличия нужных колонок
    important_columns = ["transaction_date", "status", "amount"]
    if set(important_columns).issubset(excel_data.columns):
        status = 'Ok'
    else:
        status = 'not important columns'
        excel_data = None

    return status, excel_data



status,x = read_xls('operations.xlsx')




