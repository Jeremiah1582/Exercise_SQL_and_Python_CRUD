Exercise: Setting Up and Basic SQL Commands
Backstory:
Before diving into complex database operations, you need to set up a simple database for your bookstore. This exercise will guide you through installing SQLite, creating a database, defining tables, and performing basic SQL commands.

Objective:
Set up a basic database for a bookstore and execute fundamental SQL commands.

# Tasks:
__Requirements:__
- SQLite installed on your system.
- Access to a terminal or command prompt.
- A text editor to create SQL scripts.

1)  Install SQLite:
*NOTE-If you have SQLite installed, you can skip the first step.*

Follow the instructions below to install SQLite on your system.
*For Linux:*
Open your terminal.

Run the following commands:

    $ sudo apt update
    $ sudo apt install sqlite3

*For Windows:*
Open PowerShell or Command Prompt with administrator privileges.

Run the following commands:

    $ Invoke-WebRequest -Uri "https://www.sqlite.org/2022/sqlite-tools-win32-x86-3360000.zip" -OutFile "sqlite-tools.zip"
    $ Expand-Archive -Path "sqlite-tools.zip" -DestinationPath "C:\sqlite" -Force
    $ [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\sqlite", [EnvironmentVariableTarget]::Machine)
    $ sqlite3 --version 

2) Create Database:

- Open a terminal or command prompt. 
    - Navigate to the directory where you want to create the database or specify a full path.
    - Run the following command to create the "bookstore" database file:

        $ sqlite3 

        then in sql shell...

            sqlite> .open bookstore.db
            sqlite> .quit

    Notice that this command creates a new empty SQLite database file named bookstore.db.

3) Executing SQL Commands:
- Copy the SQL script provided below into a new text file (e.g., setup.sql).
- Run the script against the SQLite database using the following command:

    $ sqlite3 bookstore.db < setup.sql

This will create tables, insert data, and perform other operations defined in the SQL script.

4) Verification:

- Open the SQLite command-line tool:

    $ sqlite3 bookstore.db

- To check if the tables are created and data is inserted, run SQL queries:

    SELECT * FROM authors; **this will List all authors**


    SELECT * FROM publishers; **this will List all publishers**


    SELECT * FROM books; **this will List all books**

Exit the SQLite shell by typing:

    sqlite> .exit

5) Update and Delete:
In the main.py file correct the mistakes in the code and: 

- using python Update the name of an author using.
- using python Delete a record from the publishers table .

# Test Case:
- Execute the SQL script to create the "bookstore" database and tables.
- Insert data into each table.
- Run queries to retrieve, update, and delete data.
