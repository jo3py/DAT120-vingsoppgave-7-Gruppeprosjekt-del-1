#Forenklet plantevekst: En forenklet modell av hvordan en plante vokser basert på
#temperatur er som følger: Planten trenger et minimum av 5 plussgrader for å vokse. Dere
#kan regne at planten sin vekst en gitt dag er lik temperatur minus
#minimumstemperaturen. Beregn total plantevekst et gitt år.

#try except få å gi feil om filen ikke fins eller eksisterer, eller om man skriver feil input

import csv

try:
    år = input("Skriv inn årstall (YYYY): ")
    if float(år) < 2014 or float(år) > 2025:
        raise ValueError
    
    total_vekst = 0

    with open(r"C:\Users\vareb\OneDrive\A UIS BACHELOR\Koder DAT-120\Github oppgaver\DAT120-vingsoppgave-7-Gruppeprosjekt-del-1\Gruppearbeid\csv_fila\sinnes_2014_2025.csv", "r", encoding="UTF-8") as fil:
        
        lest= csv.DictReader(fil, delimiter=";")

        for rad in lest:
            dato = rad["Tid(norsk normaltid)"]

            if dato.endswith(år):
                
                temp = rad["Middeltemperatur (døgn)"]

                if temp != "-":
                    temp = float(temp.replace(",", "."))

                    if temp > 5:
                        total_vekst += temp - 5

    print(f"Total plantevekst i {år}: {total_vekst:.0f}")

except ValueError:
    print("feil årstall kun 2014-2025")
except FileNotFoundError:
    print("Filenotfound")
except FileExistsError:
    print("filexistErrorr")