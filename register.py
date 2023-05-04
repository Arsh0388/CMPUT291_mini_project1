import sqlite3

def email_unique(connection: sqlite3.Connection) -> bool:
    c = connection.cursor()
    while True:
        email = input("Enter a unique email: ")
        sql_query = "SELECT email FROM members WHERE email = ?"
        c.execute(sql_query, (email,))
        if c.fetchone() is None:
            return True
        else:
            print("Email already exists. Please try again.")

        