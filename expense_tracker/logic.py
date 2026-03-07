from datetime import datetime

def sum_total(expenses):
    '''Aprēķina kopējo izdevumu summu.'''
    total = 0
    for expense in expenses:
        total += expense['amount']
    return round(total, 2)

def sum_total(expenses):
    '''Aprēķina kopējo izdevumu summu.'''
    total = 0
    for expense in expenses:
        total += expense['amount']
    return round(total, 2)

def filter_by_month(expenses, year, month):
    '''Atgriež izdevumus norādītajā gadā un mēnesī.'''
    result = []
    for expense in expenses:
        expense_date = datetime.strptime(expense['date'], '%Y-%m-%d')
        if expense_date.year == year and expense_date.month == month:
            result.append(expense)
    return result

def sum_by_category(expenses):
    '''Aprēķina summas pa kategorijām.'''
    totals = {}
    for expense in expenses:
        category = expense['category']
        totals[category] = totals.get(category, 0) + expense['amount']
    for category in totals:
        totals[category] = round(totals[category], 2)
    return totals

def get_available_months(expenses):
    '''Atgriež pieejamos mēnešus formātā YYYY-MM.'''
    months = []
    for expense in expenses:
        month = expense['date'][:7]
        if month not in months:
            months.append(month)
    months.sort()
    return months