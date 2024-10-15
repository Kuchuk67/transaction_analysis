from src.utils import read_xls, financial_period, data_formater, filter_transaction
import json
from config import PATH_HOME

def events():
    file_name ='user_settings.json'
    path_to_file = os.path.join(PATH_HOME, "data", file_name)
    with open(path_to_file) as f:
        data = json.load(f)

    print(data)

'''Курс валют.'''

'''Стоимость акций'''

events()




def transactions_by_category(transactions: dict, expenses: bool = True) -> list:
    ''' Раздел «Основные», в котором траты(поступления) по категориям отсортированы по убыванию.
    Данные предоставляются по 7 категориям с наибольшими тратами
    (поступления  не ограниченно количеством категорий),
    траты по остальным категориям суммируются и попадают в категорию «Остальное».'''
    by_category: dict[str, float] = {} # суммированные расходы по категориям
    by_category_sort: list = []  # отсортированные суммированные расходы по категориям

    for transaction in transactions:
        # циклом берем из транзакций суммы и названия категорий
        amount = round(float(transaction.get('payment_amount')), 2)
        category_in_tr = transaction.get('category')

        if expenses and amount < 0:  # расходы
            ready_category = by_category.get(category_in_tr, None)
            # если уже сохраняли такую категорию, то прибавляем к ней сумму
            if ready_category:
                by_category[category_in_tr] = round((by_category[category_in_tr] + amount), 2)
            else:
                # если категория новая, то создаем категорию и к ней сумму
                # кроме 'Переводы', 'Наличные'
                if category_in_tr not in ['Переводы', 'Наличные']:
                    by_category[category_in_tr] = amount
            # сортируем по суммам
            by_category_sort = sorted(by_category.items(), key=lambda item: item[1])


        elif not expenses and amount > 0:  # пополнения
            ready_category = by_category.get(category_in_tr, None)
            # если уже сохраняли такую категорию, то прибавляем к ней сумму
            if ready_category:
                by_category[category_in_tr] = round((by_category[category_in_tr] + amount), 2)
            else:
                # если категория новая, то создаем категорию и к ней сумму
                by_category[category_in_tr] = amount
            # сортируем по суммам
            by_category_sort = sorted(by_category.items(), key=lambda item: item[1], reverse=True)


    # В расходах отображает только первые 7 категорий
    if expenses:
        sum_other = [x[1] for x in by_category_sort[7:] ]
        by_category_result = by_category_sort[:7]
        by_category_result.append(('Другое', sum(sum_other)))
    else:
    # в пополнениях все подряд
        by_category_result = by_category_sort


    return by_category_result


def transactions_to_cash(transactions: list) -> list:
    '''Общая сумма трат наличные и переводы.'''
    sum_to_cash = sum([
                    transactions['payment_amount']
                    for transactions in transactions
                    if transactions['payment_amount'] < 0 and transactions['category'] == 'Наличные'
                    ])
    sum_transfer = sum([
        transactions['payment_amount']
        for transactions in transactions
        if transactions['payment_amount'] < 0 and transactions['category'] == 'Переводы'
    ])
    result = {'cash' : round(sum_to_cash,2), 'transfer' : round(sum_transfer,2)}
    result_sorted =  sorted(result.items(), key=lambda item: item[1], reverse=False)
    return result_sorted

def total_expenses(transactions: list) -> float:
    '''Общая сумма расходов.'''
    sum_total =  sum([transactions['payment_amount']  for transactions in transactions if transactions['payment_amount'] < 0 ])
    return sum_total

def total_receipt(transactions: list) -> float:
    '''Общая сумма поступлений.'''
    sum_total =  sum([transactions['payment_amount']  for transactions in transactions if transactions['payment_amount'] > 0 ])
    return sum_total



#status, x = read_xls('operations.xlsx')

#q = filter_transaction(x, '02.10.2021', '04.11.2021')

#w = transactions_by_category(q)
#print(w)

#w = transactions_by_category(q, expenses=True)
#print(w)

#w = total_expenses(q)
#print(w)


#w = transactions_to_cash(q)
#print(w)
