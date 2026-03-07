from datetime import date, datetime

from storage import load_expenses, save_expenses
from logic import sum_total

CATEGORIES = [
    'Ēdiens',
    'Transports',
    'Izklaide',
    'Komunālie maksājumi',
    'Veselība',
    'Iepirkšanās',
    'Cits',
]

def show_menu():
    '''Parāda izvēlni un nolasa lietotāja izvēli.'''
    print('\nIzdevumu izsekotājs')
    print('-' * 24)
    print('1) Pievienot izdevumu')
    print('2) Parādīt izdevumus')
    print('7) Iziet')
    return input('Izvēlies darbību: ').strip()

def get_date_input():
    '''Nolasa derīgu datumu.'''
    default_date = date.today().strftime('%Y-%m-%d')
    while True:
        user_input = input(f'Datums (YYYY-MM-DD) [{default_date}]: ').strip()
        if user_input == '':
            return default_date
        try:
            datetime.strptime(user_input, '%Y-%m-%d')
            return user_input
        except ValueError:
            print('Nepareizs datuma formāts. Lieto YYYY-MM-DD.')

def get_category_input():
    '''Nolasa kategoriju no saraksta.'''
    print('\nKategorijas:')
    for i, category in enumerate(CATEGORIES, start=1):
        print(f'{i}) {category}')
    while True:
        choice = input('Izvēlies kategoriju: ').strip()
        if not choice.isdigit():
            print('Ievadi kategorijas numuru.')
            continue
        choice = int(choice)
        if 1 <= choice <= len(CATEGORIES):
            return CATEGORIES[choice - 1]
        print('Tādas kategorijas nav.')

def get_amount_input():
    '''Nolasa derīgu summu.'''
    while True:
        user_input = input('Summa (EUR): ').strip().replace(',', '.')
        try:
            amount = float(user_input)
            if amount < 0:
                print('Summa nedrīkst būt negatīva.')
                continue
            return round(amount, 2)
        except ValueError:
            print('Ievadi skaitlisku vērtību.')

def get_note_input():
    '''Nolasa piezīmi.'''
    note = input('Piezīme: ').strip()
    if note == '':
        return 'Nav piezīmes'
    return note

def add_expense(expenses):
    '''Pievieno jaunu izdevumu.'''
    print('\nJauna izdevuma pievienošana')
    print('-' * 28)
    expense = {
        'date': get_date_input(),
        'amount': get_amount_input(),
        'category': get_category_input(),
        'note': get_note_input(),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(
        f'\nPievienots: {expense["date"]} | {expense["category"]} | '
        f'{expense["amount"]:.2f} EUR | {expense["note"]}'
    )

def show_expenses(expenses):
    '''Parāda visus izdevumus.'''
    head_line = '=' * 70
    row_line = '-' * 70
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        return
    print("\nIzdevumu saraksts")
    print(head_line)
    print(f'{"Nr.":>3} {"Datums":<12} {"Summa (EUR)":>12} {"Kategorija":<22} Piezīme')
    print(head_line)
    for i, expense in enumerate(expenses, start = 1):
        print(
            f'{i:>2}. '
            f'{expense["date"]:<12} '
            f'{expense["amount"]:>8.2f} EUR '
            f'{expense["category"]:<22} '
            f'{expense["note"]}'
        )
    print(row_line)
    print(f'Kopā: {sum_total(expenses):.2f} EUR | Ierakstu skaits: {len(expenses)}')
    print(row_line)

def main():
    '''Galvenā programmas cilpa.'''
    expenses = load_expenses()
    while True:
        choice = show_menu().strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '7':
            print('Programma aizvērta.')
            break
        else:
            print('Izvēlies vienu no pieejamajām darbībām.')

if __name__ == '__main__':
    main()