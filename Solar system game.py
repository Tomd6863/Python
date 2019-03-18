from tkinter import *  # import GUI
from math import *
from time import *
from random import randint

window = Tk()


def pla(x, y, r, kol):
    tlo.create_oval(x - r / 2, y - r / 2, x + r / 2, y + r / 2, fill=kol)


def rakieta(x, y, kol):
    tlo.create_rectangle(x - 2, y - 2, x + 2, y + 2, fill=kol)


def merkury():
    global szerme, wysme, katme, szerme2, wysme2
    # wyznacza środek

    szerme = szer / 2
    wysme = wys / 2
    szerme2 = szer / 2
    wysme2 = wys / 2

    # obrót
    szerme = promme * sin(katme) + szerme
    wysme = promme * -cos(katme) + wysme

    # minus bo w lewo
    katme = katme - radians(360 / 87.97)

    pla(szerme, wysme, promme1, "black")

    szerme2 = promme * sin(katme) + szerme2
    wysme2 = promme * -cos(katme) + wysme2

    pla(szerme2, wysme2, promme1, "white")


def wenus():
    global szerw, wysw, katw, szerw2, wysw2
    # wyznacza środek
    szerw = szer / 2
    wysw = wys / 2
    szerw2 = szer / 2
    wysw2 = wys / 2

    # obrót
    szerw = promw * sin(katw) + szerw
    wysw = promw * -cos(katw) + wysw

    # minus bo w lewo
    katw = katw - radians(360 / 224.7)

    pla(szerw, wysw, promw1, "black")

    szerw2 = promw * sin(katw) + szerw2
    wysw2 = promw * -cos(katw) + wysw2

    pla(szerw2, wysw2, promw1, "sandybrown")


def ksiezyc():
    global szerk, wysk, katk, szerk2, wysk2
    # wyznacza środek
    szerk = szerz2
    wysk = wysz2
    szerk2 = szerz2
    wysk2 = wysz2

    # obrót
    szerk = promk * sin(katk) + szerk
    wysk = promk * -cos(katk) + wysk

    # minus bo w lewo
    katk = katk - radians(360 / 27)
    pla(szerk, wysk, 10, "black")

    szerk2 = promk * sin(katk) + szerk2
    wysk2 = promk * -cos(katk) + wysk2

    pla(szerk2, wysk2, promk1, "grey")


def ziemia():
    global szerz, wysz, katz, szerz2, wysz2
    # wyznacza środek
    szerz = szer / 2
    wysz = wys / 2
    szerz2 = szer / 2
    wysz2 = wys / 2

    # obrót
    szerz = promz * sin(katz) + szerz
    wysz = promz * -cos(katz) + wysz

    # minus bo w lewo
    katz = katz - radians(360 / 365)

    pla(szerz, wysz, promz1, "black")

    szerz2 = promz * sin(katz) + szerz2
    wysz2 = promz * -cos(katz) + wysz2

    pla(szerz2, wysz2, promz1, "blue")


def mars():
    global szerma, wysma, katma, szerma2, wysma2
    # wyznacza środek
    szerma = szer / 2
    wysma = wys / 2
    szerma2 = szer / 2
    wysma2 = wys / 2

    # obrót w prawo
    szerma = promma * sin(katma) + szerma
    wysma = promma * -cos(katma) + wysma
    katma = katma - radians(360 / 687)

    pla(szerma, wysma, promma1, "black")

    szerma2 = promma * sin(katma) + szerma2
    wysma2 = promma * -cos(katma) + wysma2

    pla(szerma2, wysma2, promma1, "red")


def obrot():
    global licz
    # promra == promz
    licz = 1
    while promra < promma:
        pla(szer / 2, wys / 2, 20, "yellow")
        merkury()
        wenus()
        ziemia()
        ksiezyc()
        mars()

        # czeka
        sleep(0.001)
        licz += 1
        mainMenu.entryconfigure(3, label="czas = " + str(licz) + "dni")
        # odswieża ekran
        tlo.update()
    if szerra == szerma:
        wygrana()
    else:
        przegrana()


def lot2():
    global szerra, wysra, katr, szerra2, wysra2, promra, licz

    # wyznacza środek
    szerra = szer / 2
    wysra = wys / 2
    szerra2 = szer / 2
    wysra2 = wys / 2
    katr = katz

    if promra < promma:

        promra = promra + 10
        katr = katr - radians(360 / 687)

        szerra2 = promra * sin(katr) + szerra2
        wysra2 = promra * -cos(katr) + wysra2

        rakieta(szerra2, wysra2, "white")
    else:
        promra = promma

        katr = katr - radians(360 / 687)

        szerra2 = promra * sin(katr) + szerra2
        wysra2 = promra * -cos(katr) + wysra2

        rakieta(szerra2, wysra2, "white")


def wygrana():
    w = Canvas(tlo, width=szer, height=wys, bg='green')
    w.pack()
    # add string
    str1 = "Doleciałeś"
    w.create_text(szer / 2, 20, anchor=N, text=str1)


def przegrana():
    w = Canvas(tlo, width=szer, height=wys, bg='red')
    w.pack()
    # add string
    str1 = "Pudło"
    w.create_text(szer / 2, 20, anchor=N, text=str1)


szergu = 80
wysgu = 60

szer = 700
wys = 700

licz = 1

# orbity
promz = 200
promme = 0.4 * promz
promw = 0.7 * promz
promma = 1.5 * promz
promk = 0.0025 * promz + 12
promra = promz

# promienie planet
promz1 = 12
promme1 = 0.38 * promz1
promw1 = 0.95 * promz1
promma1 = 0.53 * promz1
promk1 = 0.27 * promz1

kat = 3.14 / 2

katme = randint(1, 360) * kat
katw = randint(1, 360) * kat
katz = randint(1, 360) * kat
katma = randint(1, 360) * kat
katk = randint(1, 360) * kat

mainMenu = Menu(window)
window.config(menu=mainMenu)
mainMenu.add_command(label="start", command=obrot)
mainMenu.add_separator()
mainMenu.add_command(label="czas = " + str(licz) + "dni")

tlo = Canvas(window, width=szer, heigh=wys, bg="black")

pasek = Frame(window, bg='grey', width=400, height=40)
pasek.pack(fill='x')

clickme = Button(pasek, text="start", command=lot2)
clickme.pack(side='top', padx=10)

c = Canvas(tlo, width=szer, height=wys, bg='black')

pla(szer / 2, wys / 2, 20, "yellow")
merkury()
wenus()
ziemia()
ksiezyc()
mars()

tlo.pack()

window.mainloop()  # zostawia okno otwarte
