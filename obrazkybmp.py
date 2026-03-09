# do prazdnych uvozovek patri cesta souboru
s  = open("","r+b")


s.seek(200)
s.write(b"A"*300)

zahlavi = 54
sirka = 300
x = 10
s.seek(200)
s.write(b"AAA")
# s.seek(zahlavi+x*3+sirka*3)
# s.write(b"AAA"*20)
for y in range(30,150): # svisla cara
    s.seek(zahlavi+ x*3 + y*(sirka*3))
    s.write(b"\xFF\x00\x00") # \xFF\x00\x00 rgb hodnoty ale je to naopak bgr
def scara(p,z):
    for y in range(p,z): # sikma cara
        s.seek(zahlavi+ x*3 + y*(sirka*3+1))
        s.write(b"\x00\xFF\x00")

x = int(input("Zadej kde ma cara zacinat: "))
z = int(input("Zadej kde ma cara koncit: "))

scara(x,z)

zahlavi = 54
sirka = 300
s.seek(zahlavi)
for i in range(40*sirka*3):
    pozice = s.tell()
    bod = s.read(3)
    
    novy = bod.decode("latin-1")
    novy = bytearray( [ 255-ord(novy[2]), 255-ord(novy[1]), 255-ord(novy[0]) ] )
    
    s.seek(pozice)
    s.write(novy)
s.close()