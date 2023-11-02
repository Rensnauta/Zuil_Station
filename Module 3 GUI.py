import psycopg2
import requests

station = 'Den Haag'
data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={station}&appid'
                    '=94a3f2911bac471ed9204099e905f0c9')
response = data.json()
print(response)
lst = []
connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"



def database_retrieve():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(
        """SELECT gebruikersn, datum, bericht FROM moderatie WHERE oordeel = 'goedgekeurd' order by berichtid desc limit 5""")
    data = cursor.fetchall()
    for i in data:
        naam = i[0]
        datum = i[1]
        bericht = i[2]
        opslag = '\n' + naam + ': ' + bericht + ' \n ' + datum
        lst.append(opslag)
    conn.close()

def station_service():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM station_service WHERE station_city = %s""",(station,))
    services = cursor.fetchall()
    conn.close()
    return services

station_services = station_service()

database_retrieve()

from tkinter import *
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

for i in range(len(lst)):
    label = Label(master=root,
                  text=lst[i],
                  background='#000066',
                  foreground='White',
                  font=('Helvetica', 14))
    label.pack(side='bottom', fill='x')

image = PhotoImage(file="NS.png")
label = Label(root, image=image, borderwidth=0, background='#FFCC18')
label.place(x=0, y=0)

weathericon = PhotoImage(file="Weather Icons/01d.png")
label = Label(master=root,
              image=weathericon, borderwidth=0, background='#FFCC18')
label.place(x=0, y=200)

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

database_retrieve()
