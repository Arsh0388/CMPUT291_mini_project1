import sqlite3 
from login import first_screen_login
''' getting all unseen messages  from the inbox'''
''' fetching the details after the pererson is loggedin '''



def unseen_message_display(connection: sqlite3.Connection) :
    c = connection.cursor()
    if first_screen_login() == 'yes' :
        c.execute(''' SELECT * FROM inbox
                                    WHERE email = :uname AND seen = 'n' ''')
        messages = c.fethcall()
        
        c.execute(''' UPDATE TABLE inbox
                  SET seen = 'y' 
                  WHERE email = ? AND seen = 'n', (email) ''')
        
        for i in len(messages) :
            print(messages[i])
        
        
    