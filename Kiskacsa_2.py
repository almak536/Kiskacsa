# Jövedelem számítás

print("Jövedelem számítás")

brutto = int(input("Mennyi a bruttó jövedelmed?"))
kor = int(input("Hány éves vagy ember?"))
if kor > 25:
    gyerek = input("Van 3 gyerek? (igen,nem)")
    while gyerek not in {"igen", "Igen", "i", "I", "nem", "Nem", "n", "N"}:
        print("Nem jól válaszoltál, ezek lehetnek (igen/nem)")
        gyerek = input("\nVan 3 gyerek? (igen,nem)")
if kor <= 25 or gyerek in {"igen", "Igen", "i", "I"}:
    if brutto > 500000:
        szja = (brutto - 500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15
print("ADÓ".center(40))
print("SZJA:".ljust(30, '_'), str(int(szja)).rjust(10, "_"), " Ft",  sep=(""))
print("Nyúgdíj:".ljust(30, '_'), str(int(brutto * 0.1)).rjust(10, "_"), " Ft",  sep=(""))
print("TB:".ljust(30, '_'), str(int(brutto * 0.07)).rjust(10, "_"), " Ft",  sep=(""))
print("Munkavállalói:".ljust(30, '_'), str(int(brutto * 0.015)).rjust(10, "_"), " Ft",  sep=(""))
print("")
print("Nettó:".ljust(30, '_'), str(int(brutto - szja - (brutto * 0.185))).rjust(10, "_"), " Ft",  sep=(""))
