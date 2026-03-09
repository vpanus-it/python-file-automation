# puvodni ucel kody bylo ze stranek spseol ze sekce prazdniny stahnout html soubor a pomoci tohoto kodu vypsat jednotlive prazdniny ve formatu {nazev} ; {datum}

import os 
os.system("cls")
vstup = open("", "r", encoding="latin-1") # do zavorek patri cesta souboru z ktereho chceme cist
vystupni = open("", "w",encoding="latin-1") # do zavorek patri cesta kam se vytvori novy souboru do ktereho se to bude vpisovat

while True:
    line = vstup.readline()
    if line == "":
        break
    if "zdniny" in line:
        zacatek = line.find('title="') + 7
        konec = line.find('"', zacatek)
        nazev = line[zacatek:konec]
        # print(nazev)

        data = vstup.readline()
        if data == "": # kdyz posledni radek skonci
            break
        zacatekdata = data.find('<span class="edookit_datetime">') + 31
        konecdata = data.find("<", zacatekdata)
        datum = data[zacatekdata:konecdata]
        
        print(f"{nazev} - {datum}")
        vystupni.write(f"{nazev};{datum}\n") # vypise to vedle sebe  # ";" preskoci na dalsi sloupec
vstup.close()
vystupni.close()