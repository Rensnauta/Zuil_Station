import psycopg2

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
for i in range(len(lst)):
    label = Label(master=root,
    text=lst[i],
    background='#FFCC18')
    label.pack()

root.mainloop()


database_retrieve()

