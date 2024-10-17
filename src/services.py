from src.utils import read_xls, financial_period, data_formater, filter_transaction
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from  typing  import Iterable



def increased_cashback(transactions_file: list, year: str, month: str) -> str:
    '''
    для анализа выгодности категорий повышенного кешбэка.
    На вход функции поступают данные для анализа, год и месяц.
    На выходе — JSON с анализом, сколько на каждой категории можно заработать кешбэка
     в указанном месяце года.
    '''
    data_start = f"01.{month}.{year}"
    data_iso = datetime.strptime(data_start, "%d.%m.%Y")
    data_iso = data_iso + relativedelta(months=+1, days=-1)
    data_end = datetime.strftime(data_iso, "%d.%m.%Y")

    transactions = filter_transaction(transactions_file,data_start, data_end)
    #print(transactions)

    by_category: dict[str, float] = {}  # суммированные расходы по категориям
    by_category_sort: list = []  # отсортированные суммированные расходы по категориям

    # циклом берем из транзакций суммы и названия категорий
    for transaction in transactions:

        #cashback = round(float(transaction.get('cashback'),0), 2)
        cashback = transaction.get('cashback', '')
        if cashback == '':
            cashback = 0
        cashback = float(cashback)
        #print(transaction)
        #print(cashback)
        category_in_tr = transaction.get('category')
        ready_category = by_category.get(category_in_tr, None)

        if ready_category:
            by_category[category_in_tr] = round((by_category[category_in_tr] + cashback), 2)
        else:
            by_category[category_in_tr] = cashback

        # сортируем по суммам
        by_category_sort = sorted(by_category.items(), key=lambda item: item[1], reverse=True)

    result = {}
    for category_one in by_category_sort:
        if category_one[1] > 0:
            result[category_one[0]] =  category_one[1]

    #print(result)
    return json.dumps(result,indent=4, ensure_ascii=False)



def main():
    status, transactions_file = read_xls('operations.xlsx')

    if status != 'Ok':
        result = {}
        return json.dumps(result)

    return print(increased_cashback(transactions_file, '2021', '02'))


if __name__ == "__main__":
    main()



