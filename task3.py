# task3)
# kitablar cədvəlimiz olacaq. Sütunları: adı, janrı, nəşr ili
# .2015-dən sonra nəşr olunmuş kitbaabları janrına görə artan
# sıra ilə sıralıyın
 
import sqlite3


connection = sqlite3.connect("kitablar.db")
cursor = connection.cursor()


def table_yarat():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kitablar (
            adi TEXT,
            janr TEXT,
            nesr_ili INT
        )
    """)
    connection.commit()


def elave_et_data(adi, janr, nesr_ili):
    cursor.execute("INSERT INTO kitablar VALUES (?, ?, ?)", (adi, janr, nesr_ili))
    connection.commit()


def sira_goster():
    cursor.execute("SELECT adi, janr, nesr_ili FROM kitablar WHERE nesr_ili > 2015 ORDER BY janr ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)

table_yarat()


elave_et_data('The Testaments', 'Dystopian', 2019)
elave_et_data('Becoming', 'Bioqrafiya', 2018)
elave_et_data('Educated', 'Xatire', 2014)
elave_et_data('Where the Crawdads Sing', 'Sehirli', 2018)
elave_et_data('The Silent Patient', 'Qorxulu', 2019)
elave_et_data('Circe', 'Fantastika', 2018)


sira_goster()

connection.close()
