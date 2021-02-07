import sqlite3


connection = sqlite3.connect('veterinarska_ustanova_pet_uvod.db')

# CREATE DATABASE veterinarska_ustanova_pet_uvod;

cursor = connection.cursor()

#cursor.execute('''CREATE TABLE zaposleni
 #       (licenca text, ime text, prezime text)''')

cursor.execute("INSERT INTO zaposleni VALUES ('2020110','Stefan','Simovic')")


connection.commit()

connection.close()