# task2)
# işçilər adında cədvəlimiz olacaq. Sütun olaraq ad,maaş,
# departament olacaq. Siz isə departamentinin adı satış olan 
# və maaşı 600-dən çox olan şəxslərin maaşını azalan sıra ilə 
# sıralıyın

import sqlite3


connection = sqlite3.connect("isçiler.db")
cursor = connection.cursor()


def table_yarat():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS isciler (
            ad TEXT,
            maas INT,
            departament TEXT
        )
    """)
    connection.commit()


def elave_et_data(ad, maas, departament):
    cursor.execute("INSERT INTO isciler VALUES (?, ?, ?)", (ad, maas, departament))
    connection.commit()

def sira_goster():
    cursor.execute("SELECT ad, maas FROM isciler WHERE departament='satış' AND maas > 600 ORDER BY maas DESC")
    data = cursor.fetchall()
    for row in data:
        print(row)

table_yarat()


elave_et_data('Ali', 750, 'satış')
elave_et_data('Veli', 800, 'satış')
elave_et_data('Ayşe', 600, 'satış')
elave_et_data('Fatime', 900, 'satış')
elave_et_data('Mehemmed', 500, 'satış')
elave_et_data('Semed', 700, 'satış')


sira_goster()


connection.close()
