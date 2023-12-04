# 1. Feladat: Belépés csak 18 év felett.
# Változók
kor = 16
kimenet = ""

# Feltételvizsgálat
if kor < 18:
    kimenet = "Nem léphet be!"
else:
    kimenet = "Beléphet!"

print(kimenet)

# 2. Feladat: Belépés csak 18 év felett. Kérjük be
# a kort felhasználótól!
# Változók
kor = 0
kimenet = ""

# Kor bekérése
kor = int(input("Kérem az életkorodat: "))

# Feltételvizsgálat
if kor < 18:
    kimenet = "Nem léphet be!"
else:
    kimenet = "Beléphet!"

print(kimenet)

# 3. Feladat: Három adózási kategória. 10000 Ft-ig 
# 5% ÁFA, 30000 Ft-ig 10% Áfa, fölötte 20% ÁFA.
# Kérjük be különböző termékek árát és írassuk ki
# ÁFÁ-val növelve.
# Változók
ar = 0
afasAr = 0
kimenet = ""

ar = int(input("Mennyibe kerül: "))

# Feltételvizsgálat
if ar <= 10000:
    afasAr = ar * 1.05
    kimenet = f"Áfá-s ár: {afasAr:.0f} Ft"
elif ar <= 30000:
    afasAr = ar * 1.1
    kimenet = f"Áfá-s ár: {afasAr:.0f} Ft"
else:
    afasAr = ar * 1.2
    kimenet = f"Áfá-s ár: {afasAr:.0f} Ft"

print(kimenet)

# 4. Feladat: Dolgozatjavítás során 0-50 pont elégtelen.
# 51-60 pont elégséges, 
# 61-70 pont közepes,
# 71-85 pont jó,
# 86-100 pont jeles. 
# Változók
elertPont = 0
osztalyzat = 0
kimenet = ""

elertPont = int(input("Hány pontot értél el: "))

# Feltételvizsgálat
if elertPont <= 50:
    osztalyzat = "elégtelen"
elif 51 < elertPont <= 60:
    osztalyzat = "elégséges"
elif 61 < elertPont <= 70:
    osztalyzat = "közepes"
elif 71 < elertPont <= 85:
    osztalyzat = "jó"
elif 86 < elertPont:
    osztalyzat = "jeles"

kimenet = f"Az elért eredmény: {osztalyzat}"
print(kimenet)

# 5. Feladat: Kapunk a nagymamától karácsonyra egy kis pénzt. 
# 100000 Ft-ig, Euro-ra váltjuk át.
# 200000 Ft-ig fontra és 
# 300000 Ft-ig dollárra váltjuk át.  
# Afölött meg yenre. 
# Írd ki mennyi valutát tudunk vásárolni a kapott zsebpénz függvényében.
# Változók
zsebpenz = 0
euroAr, euro = 378.70, 0
fontAr, font = 441.45, 0
dollarAr, dollar = 348.78, 0
yenAr, yen = 2.38, 0
kimenet = "A pénzem "

zsebpenz = int(input("Mennyi zsebpénzt kaptál: "))

if zsebpenz <= 100000:
    euro = zsebpenz / euroAr
    kimenet += f"{euro:.2f} eurót ér."
elif zsebpenz <= 200000:
    font = zsebpenz / fontAr
    kimenet += f"{font:.2f} fontot ér."
elif zsebpenz <= 300000:
    dollar = zsebpenz / dollarAr
    kimenet += f"{dollar:.2f} dollárt ér."
else:
    yen = zsebpenz / yenAr
    kimenet += f"{yen:.2f} yent ér."

print(kimenet)

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