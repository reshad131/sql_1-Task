# task1)
# İlk olaraq satışı reallaşmış məhsullar üçün bir cədvəl (tabel) 
# yaradırıq və bu cədvəlimizin sütun olaraq məhsul idsi, sayı və
# dəyəri (1 dənəsinin)  olacaq. Biz isə hər məhsul 
# üçün ümumi olan qazancı gətirib sıralamaq lazımdır

import sqlite3

connection = sqlite3.connect("satislar.db")
cursor = connection.cursor()


def table_yarat():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS satislar (
            muhsul_id INT,
            sayi INT,
            deyer FLOAT
        )
    """)
    connection.commit()


def elave_et_data(muhsul_id, sayi, deyer):
    cursor.execute("INSERT INTO satislar VALUES (?, ?, ?)", (muhsul_id, sayi, deyer))
    connection.commit()

def umumi_qazanc():
    cursor.execute("""
        SELECT muhsul_id, SUM(sayi * deyer) AS umumi_qazanc
        FROM satislar
        GROUP BY muhsul_id
        ORDER BY umumi_qazanc DESC
    """)
    data = cursor.fetchall()
    for row in data:
        print(row)


table_yarat()


elave_et_data(1, 10, 15)
elave_et_data(2, 5, 30)
elave_et_data(3, 7, 25)
elave_et_data(1, 3, 15)
elave_et_data(2, 2, 30)
elave_et_data(3, 8, 25)


umumi_qazanc()


connection.close()
