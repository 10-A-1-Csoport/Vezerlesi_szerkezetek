# 6. Feladat: A diákokat a nevek hossza alapján különböző csoportokba rakjuk. 5-ösével növekedjen a csoportoknak az elnevezése. Ha név több, mint 30 karaktert tartalmaz, akkor a csoport neve legyen "Leghosszabb név".
# Változok
nev = ""
nevHossz = 0
csoport = ""
kimenet = ""

nev = input("Kérem a neved: ")
nevHossz = len(nev)
kimenet = "A te csoportod: "

if nevHossz <= 5:
    csoport = "0-5"
    kimenet += csoport
elif nevHossz <= 10:
    csoport = "5-10"
    kimenet += csoport
elif nevHossz <= 15:
    csoport = "10-15"
    kimenet += csoport
elif nevHossz <= 20:
    csoport = "15-20"
    kimenet += csoport
elif nevHossz <= 25:
    csoport = "20-25"
    kimenet += csoport
elif nevHossz <= 30:
    csoport = "25-30"
    kimenet += csoport
else:
    csoport = "Leghosszabb név"
    kimenet += csoport

print(kimenet)