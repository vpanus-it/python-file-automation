# 0 od zacatku
# 1 od akt. pozice
# 2 od konce

soub = open("","rb") # cesta fotky z ktere chceme zjistit info
soub.seek(0x176)
datum = soub.read(19)
soub.close()
print(f"soubor by vyfocen {datum}")