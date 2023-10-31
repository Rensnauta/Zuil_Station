import psycopg2

berichten = []
connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"

def database_retrieve():
    berichten.clear()
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("""SELECT bericht FROM moderatie WHERE oordeel = 'goedgekeurd' order by berichtid desc limit 5""")
    data = cursor.fetchall()
    conn.close()
    for i in data:
        berichten.append(i[0])


database_retrieve()

from tkinter import *
root = Tk()

label = Label(master=root,
text=berichten[0],
background='yellow')
label.pack()

label2 = Label(master=root,
text=berichten[1],
background='yellow')
label2.pack()

label3 = Label(master=root,
text=berichten[2],
background='yellow')
label3.pack()

label4 = Label(master=root,
text=berichten[3],
background='yellow')
label4.pack()

label5 = Label(master=root,
text=berichten[4],
background='yellow')
label5.pack()

root.mainloop()