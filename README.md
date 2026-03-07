# Izdevumu izsekotājs

Šis projekts ir komandrindas Python programma personīgo izdevumu uzskaitei. Lietotājs var pievienot jaunus izdevumus, apskatīt saglabātos ierakstus, filtrēt tos pēc mēneša, redzēt kopsavilkumu pa kategorijām, dzēst ierakstus un eksportēt datus CSV failā. Programma saglabā datus JSON failā, tāpēc tie paliek saglabāti arī pēc programmas aizvēršanas.

## Uzstādīšana

1.  Noklonē repozitoriju:

```bash
git clone https://github.com/andriszeile/expense-tracker-cli.git
```
2.  Atver projekta mapi.

3.  Palaid programmu:

```bash
python expense_tracker/app.py
```

Programmai nav nepieciešamas papildu bibliotēkas.Pietiek ar Python 3.10+.

## Lietošana

Programma piedāvā šādas darbības:
 - pievienot izdevumu
 - parādīt visus izdevumus
 - filtrēt izdevumus pēc mēneša
 - apskatīt kopsavilkumu pa kategorijām
 - dzēst izdevumu
 - eksportēt datus CSV failā

Datu fails `expenses.json` izveidojas automātiski programmas darbības laikā.

## Failu struktūra
 - `expense_tracker/app.py` - galvenā programma un izvēlne
 - `expense_tracker/storage.py` - JSON failu nolasišana un saglabāšana
 - `expense_tracker/logic.py` - aprēķini un filtrēšana
 - `expense_tracker/export.py` - CSV eksports
 - `docs/plan.md` - projekta plāns
 - `docs/DEVLOG.md` - izstrādes žurnāls

## Autors

Andris