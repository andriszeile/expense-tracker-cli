# Projekta plāns

## A. Programmas apraksts

Šī programma ir vienkāršs komandrindas izdevumu izsekotājs, kas ļauj lietotājam reģistrēt savus ikdienas izdevumus. Lietotājs var pievienot jaunus izdevumus, apskatīt visus ierakstus, filtrēt tos pēc mēneša,redzēt kopsavilkumu pa kategorijām un dzēst nevajadzīgus ierakstus.

Programma saglabā visus datus JSON failā,lai tie nepazustu pēc
programmas aizvēršanas. Papildus tam lietotājs var eksportēt izdevumu sarakstu CSV failā, ko var atvērt Excel vai citā tabulu programmā.

Programmas mērķis ir praktiski apvienot vairākas Python programmēšanas pamatu tēmas vienā nelielā, bet funkcionālā lietojumā.


## B. Datu struktūra

Katrs izdevuma ieraksts tiks saglabāts kā vārdnīca ar četriem laukiem:
``` python
{
    "date": "2026-03-06",
    "amount": 12.50,
    "category": "Ēdiens",
    "note": "Pusdienas kafejnīcā"
}
```

Lauku nozīme:
 - **date** - izdevuma datums formātā `YYYY-MM-DD`
 - **amount** - iztērētā summa (decimālskaitlis)
 - **category** - izdevuma kategorija
 - **note** - īsa piezīme vai apraksts

Visi izdevumi kopā tiek glabāti sarakstā, kas tiek saglabāts JSON failā.

Piemērs:
``` python
[
    {
        "date": "2026-03-01",
        "amount": 4.80,
        "category": "Ēdiens",
        "note": "Kafija un bulciņa"
    },
    {
        "date": "2026-03-02",
        "amount": 12.00,
        "category": "Transports",
        "note": "Degviela"
    }
]
```

Šāda struktūra ir vienkārša un labi sader ar JSON formātu.


## C. Moduļu plāns

Programmā kods būs sadalīts vairākos failos, lai katrs fails atbildētu par savu funkcionalitāti.

### expense_tracker/app.py

Šis būs galvenais programmas fails. Tajā būs: - galvenā izvēlne -
lietotāja ievades apstrāde - funkciju izsaukšana no citiem moduļiem

Plānotās funkcijas:
 - show_menu() - parāda izvēlni un nolasa lietotāja izvēli
 - add_expense(expenses) - pievieno jaunu izdevumu
 - show_expenses(expenses) - parāda visus izdevumus
 - filter_expenses_menu(expenses) - filtrē izdevumus pēc mēneša
 - show_category_summary(expenses) - parāda kopsavilkumu pa kategorijām
 - delete_expense(expenses) - dzēš izdevumu pēc numura
 - export_expenses(expenses) -- eksportē izdevumus CSV failā 
 - main() - galvenā programmas cilpa

### expense_tracker/storage.py

Šis fails būs atbildīgs par datu saglabāšanu un nolasīšanu no JSON
faila.

Plānotās funkcijas: 
 - load_expenses() - nolasa izdevumus no JSON faila
 - save_expenses(expenses) - saglabā izdevumu sarakstu JSON failā

Šajā failā nebūs lietotāja ievades vai izvades.

### expense_tracker/logic.py

Šis fails saturēs funkijas, kas veic aprēķinus un datu apstrādi.

Plānotās funkcijas:
 - sum_total(expenses) - aprēķina kopējo izdevumu summu
 - filter_by_month(expenses, year, month) - filtrē izdevumus pēc
mēneša
 - sum_by_category(expenses) - aprēķina summas pa kategorijām
 - get_available_months(expenses) - atgriež mēnešus, kuros ir ieraksti

Šeit nebūs print() vai input() funkciju.

### expense_tracker/export.py

Šis fails būs atbildīgs par datu eksportu CSV formātā.

Plānotā funkcija:
 - export_to_csv(expenses, filepath) - saglabā izdevumus CSV failā

CSV failu varēs atvērt Excel vai Google Sheets.


## D. Lietotāja scenāriji

### 1. Izdevuma pievienošana

Lietotājs izvēlnē izvēlas opciju pievienot izdevumu. Programma prasa ievadīt datumu, kategoriju, summu un piezīmi. Pēc ievades programma saglabā ierakstu un parāda paziņojumu, ka izdevums pievienots.

### 2. Visu izdevumu apskate

Lietotājs izvēlas apskatīt visus izdevumus. Programma parāda tabulu ar visiem ierakstiem un kopējo summu.

### 3. Filtrēšana pēc mēneša

Lietotājs izvēlas filtrēšanas opciju. Programma parāda mēnešus, kuros ir izdevumi. Pēc izvēles tiek parādīti tikai konkrētā mēneša ieraksti.

### 4. Izdevuma dzēšana

Programma parāda numurētu izdevumu sarakstu. Lietotājs izvēlas numuru, kuru vēlas dzēst. Programma dzēš izvēlēto ierakstu.

### 5. CSV eksports

Lietotājs izvēlas eksportēt izdevumus CSV failā. Programma saglabā
failu, kuru var atvērt Excel.


## E. Robežgadījumi

Programmā jāņem vērā dažādas situācijas:
 - Ja expenses.json fails neeksistē, programma sāk ar tukšu izdevumu sarakstu.
 - Ja failā nav neviena ieraksta, programma parāda paziņojumu "Nav saglabātu izdevumu".
 - Ja lietotājs ievada tekstu summas vietā, programma parāda kļūdu un lūdz ievadīt vēlreiz.
 - Ja lietotājs ievada negatīvu summu, programma parāda kļūdas paziņojumu.
 - Ja datuma formāts nav pareizs, programma lūdz ievadīt datumu    vēlreiz.
 - Ja lietotājs mēģina dzēst ierakstu, kas neeksistē, programma parāda paziņojumu.
 - Ja filtrējot pēc mēneša nav neviena ieraksta, programma informē lietotāju.
 - Ja lietotājs ievada nepareizu izvēlnes numuru, programma lūdz   izvēlēties vēlreiz.


## Kategoriju saraksts

Programmā tiks izmantotas šādas izdevumu kategorijas:
 - Ēdiens
 - Transports
 - Izklaide
 - Komunālie maksājumi
 - Veselība
 - Iepirkšanās
 - Cits


## Papildu ideja

Ja pietiks laika, programmā varētu pievienot iespēju meklēt izdevumus pēc piezīmes teksta. Piemēram, ievadot vārdu "kafija", programma parādītu visus izdevumus, kuru piezīmē ir šis vārds.