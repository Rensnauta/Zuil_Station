import psycopg2
import requests

data = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid'
                    '=94a3f2911bac471ed9204099e905f0c9')
response = data.json()
berichten = []
lst = []
connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"

def database_retrieve():
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("""SELECT gebruikersn, datum, bericht FROM moderatie WHERE oordeel = 'goedgekeurd' order by berichtid desc limit 5""")
    data = cursor.fetchall()
    conn.close()
    for i in data:
        naam = i[0]
        datum = i[1]
        bericht = i[2]
        opslag = '\n' + naam + ': ' + bericht + ' \n ' + datum + '\n'
        lst.append(opslag)
    print(lst)

database_retrieve()


from tkinter import *
root = Tk()
root.configure(bg='#FFCC18')
for i in range(len(lst)):
    label = Label(master=root,
    text=lst[i],
    background='#FFCC18')
    label.pack()

root.mainloop()


database_retrieve()

