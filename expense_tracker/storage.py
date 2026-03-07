import json
from pathlib import Path

FILE_PATH = Path(__file__).with_name('expenses.json')

def load_expenses():
    '''Nolasa izdevumus no JSON faila.'''
    if not FILE_PATH.exists():
        return []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_expenses(expenses):
    '''Saglabā izdevumus JSON failā.'''
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)