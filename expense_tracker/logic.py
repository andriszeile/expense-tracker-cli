def sum_total(expenses):
    '''Aprēķina kopējo izdevumu summu.'''
    total = 0
    for expense in expenses:
        total += expense['amount']
    return round(total, 2)