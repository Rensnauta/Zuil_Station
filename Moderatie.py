import csv
import psycopg2
import time

connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"
lst = []

def database_upload(data):
    conn = psycopg2.connect(connection)  # verbind met de database via de connection variabele
    cursor = conn.cursor()
    query = """INSERT INTO bericht(naam, datum_bericht, tijd_bericht, station_fk, bericht, oordeel, 
    tijd_oordeel, datum_oordeel, moderator_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, data)  # voer de query uit met de data
    conn.commit()
    conn.close()


def moderatie():
    with open("berichten.csv", 'r', newline='') as file:  # open het bestand
        csv_reader = csv.reader(file)
        for row in csv_reader:  # voor iedere regel in het bestand
            print(row[0], ', ', row[4])  # print de naam en het bericht
            oordeel = input('Keurt u dit bericht goed? y/n:')
            if oordeel == 'y':  # wanneer goedgekeurd, upload naar de database
                row += ['goedgekeurd', time.strftime('%H:%M:%S'), time.strftime('%d %b %y'), mod_id]
                database_upload(row)
            elif oordeel == 'n':  # wanneer afgekeurd, upload naar de database
                row += ['afgekeurd', time.strftime('%H:%M:%S'), time.strftime('%d %b %y'), mod_id]
                database_upload(row)
            else:  # als er iets anders wordt ingevuld dan y of n
                print('Er is iets misgegaan')
                moderatie()
    with open("berichten.csv", 'w'):  # maak het bestand leeg
        pass

def inloggen():
    email = input('Email:')
    wachtwoord = input('Wachtwoord:')
    try:
        conn = psycopg2.connect(connection)  # verbind met de database via de connection variabele
        cursor = conn.cursor()
        query = "SELECT moderator_id FROM moderator WHERE email_mod = %s AND wachtwoord = %s"
        cursor.execute(query, (email, wachtwoord))
        id = cursor.fetchall()
        conn.close()
        for i in id:
            column_value = i[0]
            break
        else:
            raise ValueError()
        return id[0][0]
    except ValueError:
        print('Er is iets misgegaan')
        inloggen()



mod_id = inloggen()
moderatie()





