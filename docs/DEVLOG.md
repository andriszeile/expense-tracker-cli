# Izstrādes žurnāls

## 1. solis — plānošana

Sākumā izveidoju projekta plānu. Bija svarīgi saprast, kādi dati tiks glabāti un kādā formātā tie tiks saglabāti JSON failā. Plānošanas daļā kļuva skaidrāks,kā būs sadalītas funkcijas starp `app.py`, `storage.py`, `logic.py` un `export.py`.

## 2. solis — pamata funkcionalitāte

Šajā daļā izveidoju iespēju pievienot jaunus izdevumus, apskatīt visus ierakstus un saglabāt datus JSON failā. Tika izveidota arī kopējās summas aprēķināšana. Svarīgākais bija panākt, lai programma neuzkaras pie nepareizas ievades un lai dati saglabājas pēc aizvēršanas.

## 3. solis — filtrēšana, kopsavilkums un dzēšana

Pēc tam pievienoju filtrēšanu pēc mēneša, kopsavilkumu pa kategorijām un izdevumu dzēšanu. Šajā daļā bija jāstrādā ar datumiem, izmantojot `datetime` moduli. Vēl vajadzēja padomāt par to, kā parādīt lietotājam saprotamus paziņojumus, ja nav neviena ieraksta vai tiek ievadīts nepareizs numurs.

## 4. solis — CSV eksports un dokumentācija

Noslēgumā pievienoju CSV eksporta iespēju, lai izdevumu sarakstu varētu atvērt Excel. Tika sakārtota arī dokumentācija — izveidots `README.md` un šis izstrādes žurnāls. Šis projekts palīdzēja labāk saprast, kā sadalīt programmu moduļos un kā pakāpeniski veidot lielāku Python projektu.

## Papildinājumi un uzlabojumi

Pēc pamatfunkcionalitātes pabeigšanas tika izveidota iespēja meklēt izdevumus pēc piezīmes teksta daļas, kas ļauj ātrāk atrast konkrētus ierakstus. Meklēšana nav atkarīga no lielajiem vai mazajiem burtiem.

Papildus tika nedaudz uzlabots komandrindas interfeiss. Izvēlnē iziešanai no programmas tika nomainīta komanda `x`, kas ir intuitīvāka lietotājam nekā skaitlis.