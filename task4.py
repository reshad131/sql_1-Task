# task4)
# filmlər adlı cədvəlimiz olacaq. Sütunları : ad, çıxış tarixi,
# ratinq. Çıxış tarixi 2000-dən kiçik olanları artan sıra və 
# ratingi 7-dən böyük olanları azalan sıra ilə sıralıyın

import sqlite3

connection = sqlite3.connect("filmler.db")

cursor = connection.cursor()

def table_yarat():
    cursor.execute("CREATE TABLE IF NOT EXISTS filmler (ad TEXT, rejissor TEXT, buraxilis_ili INT, uzunluq INT)")
    connection.commit()

def elave_et_data():
    cursor.execute("INSERT INTO filmler VALUES ('Fight club', 'David Fincher', 1999, 139)")
    connection.commit()

def dynamic_elave_et_data(ad, rejissor, buraxilis_ili, uzunluq):
    cursor.execute("INSERT INTO filmler VALUES (?, ?, ?, ?)", (ad, rejissor, buraxilis_ili, uzunluq))
    connection.commit()

def data_goster():
    cursor.execute("SELECT * FROM filmler")
    data = cursor.fetchall()
    for row in data:
        print(row)

def dynamic_data_goster(rejissor):
    cursor.execute("SELECT ad FROM filmler WHERE rejissor=?", (rejissor,))
    data = cursor.fetchall()
    for row in data:
        print(row)

def duzelt(old_uzunluq, new_uzunluq):
    cursor.execute("UPDATE filmler SET uzunluq = ? WHERE uzunluq = ?", (new_uzunluq, old_uzunluq))
    connection.commit()

def datani_sil(ad):
    cursor.execute("DELETE FROM filmler WHERE ad = ?", (ad,))
    connection.commit()

table_yarat()
elave_et_data()

ad = input("Filmin adı: ")
rejissor = input("Rejissor: ")
buraxilis_ili = int(input("İl: "))
uzunluq = int(input("Uzunluq: "))
dynamic_elave_et_data(ad, rejissor, buraxilis_ili, uzunluq)

rejissor = input("Rejissoru daxil edin: ")


connection.close()