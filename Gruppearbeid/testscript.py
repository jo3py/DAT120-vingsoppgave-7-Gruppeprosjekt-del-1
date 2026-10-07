import csv

try:
    år = input("Skriv inn årstall (YYYY)")
    if float(år)<2014 or float(år)>2025:
        raise ValueError
    total_plantevekst=0
    with open(r"C:\Users\vareb\OneDrive\A UIS BACHELOR\Koder DAT-120\Github oppgaver\DAT120-vingsoppgave-7-Gruppeprosjekt-del-1\Gruppearbeid\csv_fila\sinnes_2014_2025.csv", "r", encoding="UTF-8") as fil:
            lest= csv.DictReader(fil, delimiter=";")

            for rad in lest:
                 dato = rad["Tid(norsk normaltid)"]

                 if dato.endswith(år):

                      temp= rad["Middeltemperatur (døgn)"]

                      if temp != "-":
                           temp= float(temp.replace(",","."))

                           if temp>5:
                                total_plantevekst+= temp
    print(f"total_plantevekst i{år} var: {total_plantevekst:.0f}")
except ValueError:
     print("feil år")