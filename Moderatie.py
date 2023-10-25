import csv


def moderatie():
    with open("berichten.csv", 'r', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            print(row[3])
            oordeel = input('Keurt u dit bericht goed? y/n: ')
            if oordeel == 'y':
                with open('moderatie.csv', 'a') as file:
                    row.append('goedgekeurd')
                    csv.writer(file).writerow(row)
            elif oordeel == 'n':
                with open('moderatie.csv', 'a') as file:
                    row.append('afgekeurd')
                    csv.writer(file).writerow(row)


moderatie()