import csv
import psycopg2
import time


email = 'voorbeeld123@email.com'
naam_mod = 'moderator1'
connection = "host='20.254.33.20' dbname='stationszuil' user='postgres' password='Welkom01!'"


def database_upload(data):
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    query = """INSERT INTO moderatie (gebruikersn, datum, tijd, station, bericht, oordeel, tijdoordeel, 
    datumoordeel,  emailmod, naammod) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, data)
    conn.commit()
    conn.close()


with open("moderatie.csv", 'w', newline='') as f:
    pass


def moderatie():
    with open("berichten.csv", 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[4])
            oordeel = input('Keurt u dit bericht goed? y/n:')
            if oordeel == 'y':
                row += ['goedgekeurd', time.strftime('%H:%M:%S'), time.strftime('%d %b %y'), email, naam_mod]
                database_upload(row)
            elif oordeel == 'n':
                row += ['afgekeurd', time.strftime('%H:%M:%S'), time.strftime('%d %b %y'), email, naam_mod]
                database_upload(row)
            else:
                print('Er is iets misgegaan')
                moderatie()


moderatie()
