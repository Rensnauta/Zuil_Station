import csv
import time
import random

with open("berichten.csv", 'w', newline='') as f:
    csv_writer = csv.writer(f)


def selecteer_station():
    with open('stations.txt', 'r') as file:  # open het bestand met alle stations
        stations = (file.read().splitlines())  # sla de inhoud op in een lijst
        keuze = random.choice(stations)  # kies een random station uit de lijst
        return keuze


def input_naam():  # creeër een functie om de naam van een bezoeker te vragen
    naam = input("Wat is uw naam?")
    if len(naam) == 0:
        print('Uw bericht wordt anoniem geplaatst')
        naam = 'Anoniem'
        return naam
    elif len(naam) < 51:  # bepaal of de ingevoerde naam niet te lang is
        return naam  # sla de naam op als variabele
    else:  # als de naam die de bezoeker heeft ingevuld te lang is
        print("Uw naam is te lang")
        input_naam()  # herhaal de functie, vraag om een nieuwe input


def input_bericht():  # creeër een functie om het bericht van een bezoeker te krijgen
    bericht = input("Wat wilt u melden?")
    if len(bericht) < 141:  # bepaal of het bericht niet te lang is
        message = bericht
        return message
    else:
        print("Uw bericht is te lang")
        input_bericht()


def output_csv():  # functie die het bericht met de data wegschrijft naar het csv-bestand
    with open("berichten.csv", "a", newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([naam, time.strftime('%d %b %y'), time.strftime('%H:%M:%S'), station, bericht])


while True:  # loop die allefuncties herhaalt
    selecteer_station()
    naam = input_naam()
    bericht = input_bericht()
    station = selecteer_station()
    output_csv()
