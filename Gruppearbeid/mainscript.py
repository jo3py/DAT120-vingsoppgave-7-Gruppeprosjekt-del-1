from oppgave_d import plotting_av_data
from oppgave_h import teller_sommedager

startverdi = True
while startverdi:
    try:
        aarstall = input("Skriv inn aarstall (yyyy): ")
        intervall = int(aarstall)
        if intervall >= 2014 and intervall <= 2025:
            startverdi = False
        else:
            print("Årstallet må være i mellom 2014 og 2025")
            startverdi = True
    except ValueError:
        print("Ugyldig input. Skriv inn et årstall.")
        startverdi = True



plotting_av_data(aarstall)
teller_sommedager(aarstall)