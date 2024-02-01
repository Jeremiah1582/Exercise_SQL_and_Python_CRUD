''' 
NOTE:

    bookstore.db should be created and 
    populated before continuing

'''

import sqlite3
from pathlib import Path
import os
from time import sleep

# change directory
path= Path(__file__).parent
os.chdir(path)

# 1) CONNECT
conn = sqlite3.connect('./bookstore.db')

    # create cursor
cursor= conn.cursor()
# READ_1
sql_query = 'SELECT * FROM authors'
cursor.execute(sql_query)
records = cursor.fetchall()
for record in records: 
    print(record)
    
# UPDATE
sql_update_query = "UPDATE authors SET author_name = 'Jeremiah Brown' WHERE author_id = 1;"
cursor.execute(sql_update_query)
conn.commit() #commit changes to database

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

try:
    
    # INSERT/CREATE
    # sleep(5)#sleep for 20s then delete the file
    sql_insert_query = 'INSERT INTO authors (author_id, author_name) VALUES(10,"Test_name");'
    cursor.execute(sql_insert_query)
    conn.commit() #
except Exception:
    print(Exception.with_traceback())
    
    # you can view the change in Database
    
# 5) DELETE
try: 
    sleep(20) 
    sql_delete_query= 'DELETE FROM authors WHERE author_id = 10'
    cursor.execute(sql_delete_query)

    deleted_record= cursor.fetchone()

    print('deleted record is:....')
    conn.commit()
    # You will see in the table that the record was deleted
except Exception:
    print(Exception.with_traceback())
 
# READ 3
sql_query = 'SELECT * FROM authors'
cursor.execute(sql_query)
records = cursor.fetchall()
for record in records: 
    print(record)