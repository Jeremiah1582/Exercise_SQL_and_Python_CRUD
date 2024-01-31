import sqlite3
from pathlib import Path

''' 
NOTE:

    bookstore.db should be created and 
    populated before continuing

'''

# 1) CONNECT
conn = sqlite3.connect('bookstore.db')

    # create cursor
cursor= conn.cursor()
# READ_1
sql_query = 'SELECT * FROM authors'
cursor.execute(sql_query)
records = cursor.fetchall()
for record in records: 
    print(record)
    
# UPDATE
sql_update_query = 'UPDATE authors SET author_name = "Jeremiah Brown" WHERE "author_id" = 1;'
cursor.execute(sql_update_query)

# READ_2
sql_query = 'SELECT * FROM authors'
cursor.execute(sql_query)
records = cursor.fetchall()
for record in records: 
    print(record)


new_records=cursor.fetchall()
print(new_records)
for rec in new_records: 
    print(rec)

# 5) DELETE