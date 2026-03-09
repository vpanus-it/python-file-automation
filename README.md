# python-file-automation
# Python File Automation & Byte Manipulation

Tento repozitář obsahuje sbírku skriptů pro automatizované zpracování souborů a manipulaci s daty. Ukazuje schopnost pracovat jak s textovými daty, tak s binárními formáty na nízké úrovni.

## Obsažené skripty a jejich funkce

### 1. Parsování dat (`spseol_prazdniny.py`)
Skript analyzuje poskytnutý HTML soubor, vyhledává specifické značky a extrahuje potřebná data (např. názvy a data školních prázdnin). Následně tato strukturovaná data exportuje a zapisuje do čistého formátu `.csv` pro další využití (např. v Excelu).

### 2. Binární úprava BMP obrázků (`obrazkybmp.py`)
Skript otevírá soubory ve formátu `.bmp` v binárním režimu (`r+b`). Ukazuje pochopení struktury hlavičky BMP souboru (offset dat) a využívá metodu `seek()` k přímému zápisu hexadecimálních RGB hodnot (respektive BGR) na konkrétní souřadnice pro programové vykreslování tvarů a čar přímo do binárního kódu obrázku.

### 3. Čtení z konkrétních pozic (`cteni_z_pozic.py`)
Skript demonstruje navigaci v souborech (absolutní i relativní pozicování) a extrakci konkrétních bajtových úseků.

## Technologie
* Python 3
* Souborový I/O (čtení/zápis textu i binárních dat)
* Znalost hlaviček souborů (BMP formát)
* Kódování znaků (Latin-1, UTF-8)
