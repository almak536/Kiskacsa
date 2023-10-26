from tkinter import * # nézd meg ezt h tényleg így kell e csinálni


def belepes_ablak():

    def ok_gomb_kezelese():
        belepes.destroy()

    def reg_gomb_kezelese():
        belepes.destroy()


    belepes = Tk()
    belepes.title("Belépés")

    felh_nev_cimke = Label(belepes, text="Felhasználó neve (Emal): ")
    felh_jelszo_cimke = Label(belepes, text="Jelszo: ")

    felh_nev = Entry(belepes, width=30)
    felh_jelszo = Entry(belepes, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_kezelese)




    felh_nev_cimke.grid(row=0, column=0, pady=20, padx=10, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, sticky=E, padx=10)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, sticky=W, padx=10)
    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_reg.grid(row=2, column=1)






    belepes.mainloop()

def reg_ablak(): # Ezt fejezd be majd ottthon, úgy kell csomálni mint otthon
    pass
