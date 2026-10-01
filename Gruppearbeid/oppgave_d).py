#   Plotting: Dere skal la brukeren skrive inn et årstall og så skal programmet plotte
#   snødybde, nedbør, middeltemperatur og høyeste middelvind hver dag for dette året.
#   Hint: Konverter datoene fra strenger til datetime objekter for å få en finere visning av
#   datoene
import csv
import matplotlib.pyplot as plt
from datetime import datetime

snodybde = []
nedbor = []
middeltemperatur = []
hoyeste_middelvind = []
dato = []

aarstall = input("Skriv inn dato (yyyy): ")
with open("GitHub/DAT120-vingsoppgave-7-Gruppeprosjekt-del-1/Gruppearbeid/csv_fila/sinnes_2014_2025.csv",
           "r", encoding = "UTF-8") as fila:
    leser = csv.reader(fila , delimiter=";")
    next(leser)
    for rad in leser:
        if aarstall in rad[2]:
            snodybde1 = rad[6].replace("-","0")
            snodybde.append(float(snodybde1))

            nedbor1 = rad[4].replace(",",".")
            nedbor.append(float(nedbor1))

            middeltemperatur1 = rad[3].replace(",",".").replace("-","0")
            middeltemperatur.append(float(middeltemperatur1))

            middelvind1 = rad[5].replace(",",".").replace("-","0")
            hoyeste_middelvind.append(float(middelvind1))
            #dato1 = rad[2].split(".")
            #dato2 = (dato1[0:2])
            #dato.append(dato2)
            dato.append(datetime.strptime(rad[2], "%d.%m.%Y"))
    print()
    print(type(dato[0]))
    #print(type(datoer[0]))
    print(type(snodybde[0]))
    print()
    plt.subplot (2, 2, 1)
    plt.plot(dato, snodybde, label = "Snødybde i " + aarstall)
    plt.ylim(min(snodybde), max(snodybde))
    plt.legend()

    plt.subplot (2, 2, 2)
    plt.plot(dato, nedbor, label = "Nedbør i " + aarstall)
    plt.legend()

    plt.subplot (2, 2, 3)
    plt.plot(dato, middeltemperatur, label = "Middeltemperatur i " + aarstall)
    plt.legend()

    plt.subplot (2, 2, 4)
    plt.plot(dato, hoyeste_middelvind, label = "Høyeste_middelvind i " + aarstall)
    plt.legend()
    plt.show()
