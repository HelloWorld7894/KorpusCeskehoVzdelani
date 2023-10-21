# Korpus Českého Vzdělání

## Program
Tahle webová stránka slouží jako shrnutí českého školství pomocí mapy české republiky rozdělené na kraje.
**Funkce:**
- Porovnávání ukazatelů mezi kraji
- Hodnocení školy pomocí ChatGPT

***Odkaz na webovou aplikaci:*** http://tomeng.rf.gd/SusiceHack/templates/

**Jak program funguje:**
1. Stáhne aktuální datové sady pro porovnávání krajů
2. Podle uživatelského vstupu se vyhledá příslušná škola k vyhodnocení ChatGPT (bodové rozhraní je od 0 do 10)
3. Vyhodnotí do 5 záznamů z ČSI (české školní inspekce)
4. Poslání vyhodnocených dat na web


**z jakých datových zdrojů jsme čerpali:**

* **Registr inspekčních zpráv ČSI** (https://www.csicr.cz/cz/Registr-inspekcnich-zprav) - zprávy české školní inspekce ze všech škol

* **Vzdělávání ČSU** (https://www.czso.cz/csu/czso/1-vzdelavani) - počet studentů ve vzdělávání podle věku, pohlaví a tříd
    * Data: [ČSÚ VDB](https://vdb.czso.cz/vdbvo2/faces/index.jsf?page=statistiky&filtr=G~F_M~F_Z~F_R~F_P~_S~_null_null_&katalog=30848)

## Datové sady a jejich anotace

***Školství***

* **Vzdělávání ČSU** (https://www.czso.cz/csu/czso/1-vzdelavani) - počet studentů ve vzdělávání podle věku, pohlaví a tříd
    * Data: [ČSÚ VDB](https://vdb.czso.cz/vdbvo2/faces/index.jsf?page=statistiky&filtr=G~F_M~F_Z~F_R~F_P~_S~_null_null_&katalog=30848)

* **Registr inspekčních zpráv ČSI** (https://www.csicr.cz/cz/Registr-inspekcnich-zprav) - zprávy české školní inspekce ze všech škol

* **Statistická data o ICT na školách MŠMT** (https://www.msmt.cz/vzdelavani/skolstvi-v-cr/statistika-skolstvi/otevrena-data) - počet počítačů a všeho ostatního co se týká ICT

* **Rejstřík škol a školských zařízení** (http://stistko.uiv.cz/registr/vybskolrn.asp) - informace o tom o jakou organizaci se jedná, kontaktní osoba a další info o specifické škole

***Ostatní povolené data***

* **Výsledky sčítání obyvatel 2021** ([scitani-otevrena-data-2021](https://www.czso.cz/csu/czso/vysledky-scitani-2021-otevrena-data))

    Např.:
    * Obyvatelstvo podle rodinného stavu
    * Obyvatelstvo podle náboženství
    * Obyvatelstvo podle vzdělání

* **Uchazeči o zaměstnání dosažitelní a podíl nezaměstnaných osob podle obcí** ([uchazeci-o-zamestnani-podle-obci](https://www.czso.cz/csu/czso/uchazeci-o-zamestnani-dosazitelni-a-podil-nezamestnanych-osob-podle-obci_090417))

* **Registr ekonomických subjektů** (https://www.czso.cz/csu/czso/registr-ekonomickych-subjektu-otevrena-data) - I školy jsou ekonomické subjekty

## Datové sady které jsou už v souborech

*všechno se to nachází na ms teams

* **Adresář středních škol** (<ins>Adresar SŠ CR.xls</ins>) - adresář škol, název, zkrácený název, atd.

* **Aktivity SŠ** (<ins>Klíčové aktivity.xlsx</ins>)

* **Projekty SŠ** (<ins>Přehled projektů - výzva 02_22_003 OPJAK.xlsx</ins>)

* **Seznamy žáků a studentů** (<ins>Seznamy_zaku_studentu_SS_VOS_DM_INT_2021_web.xlsx</ins>) - počet žáků SŠ a VOŠ

* regionální statistiky region/okres/kraj/stat(<ins>UZEMI-KODY_obec_pou_orp_okres_kraj_region-stat.xlsx</ins>)

* ****
## Inspirace na vykreslování

* **geodata ČSÚ** ([geodata.statistika.cz](https://geodata.statistika.cz/portal/apps/sites/#/homepage)) - vizualizace dat a georeport

