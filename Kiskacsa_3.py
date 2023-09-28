# Számológép


def adatkeres(tipus):
    valasz = 0
    if tipus == "sz":
        valasz = input("Kérek egy számot: ")
        while not valasz.isalnum():
            print("Hibás szám!!!")
            valasz = input("Kérek egy számot: ")
        valasz = int(valasz)
    elif tipus == "m":
        valasz = input("Milyen művelet legyen? (+,-,*,/)")
        while valasz not in ["+", "-", "*", "/"]:
            print("Nem jó műveleti kód!!!")
            valasz = input("Milyen művelet legyen? (+,-,*,/): ")
    return valasz

def szamitas():
    eredmeny = 0

    if muvelet == "+":
        eredmeny = szam1 + szam2
    elif muvelet == "-":
        eredmeny = szam1 - szam2
    elif muvelet == "*":
        eredmeny = szam1 * szam2
    else:
        eredmeny = szam1 / szam2
    return eredmeny

# a program indítási pontja
print("Számológép")
szam1 = adatkeres("sz")
muvelet = adatkeres("m")
szam2 = adatkeres("sz")
vegeredmeny = szamitas()



"""muvelet = input("Milyen művelet legyen? (+,-,*,/)")
while muvelet not in ["+", "-", "*", "/"]:
    print("Nem jó műveleti kód!!!")
    muvelet = input("Milyen művelet legyen? (+,-,*,/): ")"""

"""szam2 = input("Kérek egy számot: ")
while not szam2.isalnum():
    print("Hibás szám!!!")
    szam2 = input("Kérek egy számot: ")
szam2 = int(szam2)"""

"""eredmeny = 0

if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
else:
    eredmeny = szam1 / szam2"""

print(str(szam1).rjust(50))
print(muvelet, sep="")
print(str(szam2).rjust(49))
print("".rjust(50, "-"))
print(str(vegeredmeny).rjust(50))


