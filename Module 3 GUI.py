import psycopg2
import requests
from tkinter import *

lst = []


def station_selectie():  # GUI waar een station geselecteerd kan worden
    root = Tk()
    root.title()
    root.configure(bg='#FFCC18')
    root.geometry("800x400")
    image = PhotoImage(file="NS.png")
    label = Label(root, image=image, borderwidth=0, background='#FFCC18')
    label.place(x=0, y=0)
    option_label = Label(root, text="Selecteer uw station",
                         background='#000066',
                         foreground='White',
                         font=('Helvetica', 25))
    option_label.pack()
    stations = ["Deventer", "Den Haag", "Hengelo"]
    geselecteerd = StringVar()
    dropdown = OptionMenu(root, geselecteerd, *stations)  # dropdownmenu met 3 stations
    dropdown.pack()
    send_button = Button(root, text="Bevestigen", command=lambda: root.destroy())
    send_button.pack()
    root.mainloop()
    return geselecteerd.get()


station = station_selectie()  # slaat het geselecteerde station op
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={station}&appid"
                    "=94a3f2911bac471ed9204099e905f0c9&units=metric")  # API-url
response = data.json()
# sla de benodige waardes op in variabelen
weathericon = response['weather'][0]['icon'] + '.png'
weatherdescription = response['weather'][0]['description']
temperature = response['main']['temp']
weerbericht = str(weatherdescription) + '\n' + str(temperature) + '°C'
# connectiestring voor de database
connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"


def database_retrieve(): # functie om de goedgekeurde berichten uit de database te halen
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(
        "select bericht.naam, bericht.datum_bericht, bericht.bericht from moderator "
        "full join bericht on bericht.moderator_id = moderator.moderator_id "
        "full join station_service on station_service.station_city = bericht.station_fk "
        "where oordeel = 'goedgekeurd' order by bericht_id desc limit 5")
    data = cursor.fetchall()
    for i in data:  # haal de waardes uit een lijst en sla ze op in losse variabelen
        naam = i[0]
        datum = i[1]
        bericht = i[2]
        opslag = '\n' + naam + ': ' + bericht + ' \n ' + str(datum)  # voeg de variabelen samen tot een string
        lst.append(opslag)
    conn.close()  # sluit de connectie


def station_service():  # functie om de services die aanwezig zijn op het station te bepalen
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM station_service WHERE station_city = %s""", (station,))
    services = cursor.fetchall()
    conn.close()
    return services


station_services = station_service()

database_retrieve()

root = Tk()
root.title(station)
root.configure(bg='#FFCC18')
root.geometry("600x800")

label = Label(master=root,
              text=station,
              background='#FFCC18',
              foreground='#000066',
              font=('Helvetica', 25, 'bold'))
label.pack(side='top')

for i in range(len(lst)):  # maakt voor ieder bericht een label aan in de GUI
    label = Label(master=root,
                  text=lst[i],
                  background='#000066',
                  foreground='White',
                  font=('Helvetica', 14))
    label.pack(side='bottom', fill='x')

image = PhotoImage(file="NS.png")  # voegt het NS logo linksboven toe
label = Label(root, image=image, borderwidth=0, background='#FFCC18')
label.place(x=0, y=0)

weathericon = PhotoImage(file=f"Weather Icons/{weathericon}")  # plaats een icoon bij het weerbericht
label = Label(master=root,
              image=weathericon, borderwidth=0, background='#FFCC18')
label.place(x=0, y=200)

label = Label(master=root,
              text=weerbericht,
              background='#FFCC18')
label.place(x=15, y=300)

# de volgende blokken code bepalen voor elke service of het aanwezig is op het station een plaats indien nodig
# een afbeelding van de service
if station_services[0][2] is True:
    ov_fiets = PhotoImage(file="img_ovfiets.png")
    label = Label(root, image=ov_fiets, borderwidth=0, background='#FFCC18')
    label.pack(anchor='ne')
else:
    pass

if station_services[0][3] is True:
    lift = PhotoImage(file="img_lift.png")
    label = Label(root, image=lift, borderwidth=0, background='#FFCC18')
    label.pack(anchor='ne')
else:
    pass

if station_services[0][4] is True:
    toilet = PhotoImage(file="img_toilet.png")
    label = Label(root, image=toilet, borderwidth=0, background='#FFCC18')
    label.pack(anchor='ne')
else:
    pass

if station_services[0][5] is True:
    P_R = PhotoImage(file="img_pr.png")
    label = Label(root, image=P_R, borderwidth=0, background='#FFCC18')
    label.pack(anchor='ne')
else:
    pass

root.mainloop()


