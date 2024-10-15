from src.utils import read_xls, financial_period, data_formater, filter_transaction

def events() -> str:
    pass


'''«Расходы»:
Общая сумма расходов.
Раздел «Основные», в котором траты по категориям отсортированы по убыванию. Данные предоставляются по 7 категориям с наибольшими тратами, траты по остальным категориям суммируются и попадают в категорию «Остальное».
Раздел «Переводы и наличные», в котором сумма по категориям «Наличные» и «Переводы» отсортирована по убыванию.'''




'''«Поступления»:
Общая сумма поступлений.
Раздел «Основные», в котором поступления по категориям отсортированы по убыванию.'''



'''Курс валют.'''


'''Стоимость акций'''

def transactions_by_category(transactions: dict, expenses: bool=True) -> dict:
    ''' Раздел «Основные», в котором траты(поступления) по категориям отсортированы по убыванию.
    Данные предоставляются по 7 категориям с наибольшими тратами
    (поступления  не ограниченно количеством категорий),
    траты по остальным категориям суммируются и попадают в категорию «Остальное».'''
    by_category: dict =  {}
    for transaction in transactions:
        category_in_tr = transaction.get('category')
        category = by_category.get(category_in_tr, None)
        if category:
            by_category[category_in_tr] += transaction.get('payment_amount')
        else:
            by_category[category_in_tr] = transaction.get('payment_amount')
    return by_category

status,x = read_xls('operations.xlsx')
#print(x[0])
q = filter_transaction(x,'14.01.2021','14.11.2021')

w = transactions_by_category(q)

#print(*q, sep='\n')
print(w)


