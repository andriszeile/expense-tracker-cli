from datetime import date, datetime

from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months, search_by_note
from export import export_to_csv

WIDTH = 80
LINE = "-" * WIDTH
HEADER_LINE = "=" * WIDTH

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
    print(HEADER_LINE)
    print('Izdevumu izsekotājs')
    print(HEADER_LINE)
    print('1) Pievienot izdevumu')
    print('2) Parādīt izdevumus')
    print('3) Filtrēt pēc mēneša')
    print('4) Kopsavilkums pa kategorijām')
    print('5) Dzēst izdevumu')
    print('6) Eksportēt CSV')
    print('7) Meklēt pēc piezīmes')
    print('x) Iziet')
    return input('Izvēlies darbību: ').strip()

def pause():
    '''Pause, lai lietotājs var apskatīt rezultātu, pirms izvēlnes parādīšanas.'''
    input('\n***Nospied Enter, lai redzētu izvēlni...***')

def print_expenses_table(expenses, title):
    '''Izdevumu tabulas vienotais formāts izdrukai.'''
    print(f'\n{title}')
    print(HEADER_LINE)
    print(f'{"Nr.":>4} {"Datums":<12} {"Summa (EUR)":>12} {"Kategorija":<21} Piezīme')
    print(HEADER_LINE)
    for i, expense in enumerate(expenses, start = 1):
        print(
            f'{i:>3}) '
            f'{expense["date"]:<12} '
            f'{expense["amount"]:>8.2f} EUR '
            f'{expense["category"]:<22}'
            f'{expense["note"]} '
        )
    print(LINE)

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
    expense = {
        'date': get_date_input(),
        'amount': get_amount_input(),
        'category': get_category_input(),
        'note': get_note_input(),
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(LINE)
    print(
        f'Pievienots: {expense["date"]} | {expense["category"]} | '
        f'{expense["amount"]:.2f} EUR | {expense["note"]}'
    )
    pause()

def show_expenses(expenses):
    '''Parāda visus izdevumus.'''
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        pause()
        return
    print_expenses_table(expenses, 'Izdevumu saraksts')
    print(f'Kopā: {sum_total(expenses):.2f} EUR | Ierakstu skaits: {len(expenses)}')
    pause()

def filter_expenses_menu(expenses):
    '''Parāda izdevumus izvēlētajā mēnesī.'''
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        pause()
        return
    months = get_available_months(expenses)
    if not months:
        print('\nNav pieejamu mēnešu filtrēšanai.')
        pause()
        return
    print('\nPieejamie mēneši:')
    for i, month in enumerate(months, start=1):
        print(f'{i}) {month}')
    while True:
        choice = input('Izvēlies mēnesi: ').strip()
        if not choice.isdigit():
            print('Ievadi mēneša numuru.')
            continue
        choice = int(choice)
        if 1 <= choice <= len(months):
            selected_month = months[choice - 1]
            break
        print('Izvēlies derīgu mēneša numuru.')
    year, month = selected_month.split('-')
    filtered = filter_by_month(expenses, int(year), int(month))
    if not filtered:
        print('\nŠajā mēnesī izdevumu nav.')
        pause()
        return
    print_expenses_table(filtered, f'\nIzdevumi par {selected_month}')
    print(f'Kopā: {sum_total(filtered):.2f} EUR | Ierakstu skaits: {len(filtered)}')
    pause()

def show_category_summary(expenses):
    '''Parāda kopsavilkumu pa kategorijām.'''
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        pause()
        return
    totals = sum_by_category(expenses)
    print(HEADER_LINE)
    print('Kopsavilkums pa kategorijām')
    print(HEADER_LINE)
    for category, total in totals.items():
        print(f'{category:<22} {total:>8.2f} EUR')
    print(LINE)
    print(f'Kopā: {sum_total(expenses):.2f} EUR')
    pause()

def delete_expense(expenses):
    '''Dzēš izdevumu pēc numura.'''
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        pause()
        return
    print_expenses_table(expenses, '\nSaglabātie izdevumi')
    while True:
        choice = input('Kuru ierakstu dzēst? (0 - atcelt): ').strip()
        if not choice.isdigit():
            print('Ievadi ieraksta numuru.')
            continue
        choice = int(choice)
        if choice == 0:
            print('Dzēšana atcelta.')
            pause()
            return
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(
                f'\nDzēsts: {removed["date"]} | {removed["amount"]:.2f} EUR | '
                f'{removed["category"]} | {removed["note"]}'
            )
            pause()
            return
        print('Tāda ieraksta numura nav.')

def export_expenses(expenses):
    '''Eksportē izdevumus CSV failā.'''
    if not expenses:
        print('\nNav saglabātu izdevumu eksportēšanai.')
        return
    filename = input('Faila nosaukums [izdevumi.csv]: ').strip()
    if filename == '':
        filename = 'izdevumi.csv'
    if not filename.lower().endswith('.csv'):
        filename += '.csv'
    export_to_csv(expenses, filename)
    print(f'\nEksportēts: {len(expenses)} ieraksti -> {filename}')
    pause()

def search_expenses(expenses):
    '''Meklē izdevumus pēc piezīmes teksta.'''
    if not expenses:
        print('\nNav saglabātu izdevumu.')
        pause()
        return
    search_text = input('Ievadi meklējamo tekstu: ').strip()
    if search_text == '':
        print('Meklēšanas teksts nav tukšums.')
        pause()
        return
    results = search_by_note(expenses, search_text)
    if not results:
        print(f'\nNav atrasts neviens ieraksts ar tekstu "{search_text}".')
        pause()
        return
    print_expenses_table(results, f'\nMeklēšanas rezultāti tekstam "{search_text}"')
    print(f'Atrasti ieraksti: {len(results)} | Summa: {sum_total(results):.2f} EUR')
    pause()

def main():
    '''Galvenā programmas cilpa.'''
    expenses = load_expenses()
    while True:
        choice = show_menu().strip()
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            filter_expenses_menu(expenses)
        elif choice == '4':
            show_category_summary(expenses)
        elif choice == '5':
            delete_expense(expenses)
        elif choice == '6':
            export_expenses(expenses)
        elif choice == '7':
            search_expenses(expenses)
        elif choice == 'x':
            print('Programma aizvērta.')
            break
        else:
            print('Izvēlies vienu no pieejamajām darbībām.')

if __name__ == '__main__':
    main()