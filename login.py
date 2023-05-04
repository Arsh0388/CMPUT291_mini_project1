# reference matereial 
# cmput 291 lab material for verified and secure login 
# to avoid sql injection attack 
# https://medium.com/opex-analytics/database-connections-in-python-extensible-reusable-and-secure-56ebcf9c67fe used for passing databse connection to other function
import sys
import sqlite3
from  register import email_unique 

connection = sqlite3.connect('./sql.db')
c = connection.cursor()
def main_function() :
    valid_input = input("if you already have an account then login by typing login and if you are a new customer then register by typing r")
    
    if valid_input.lower() == "login" :
        email_address = input("enter your email address ")
        password = input("enter your password")
        return first_screen_login(email_address,password)
        
def first_screen_login(email,password) :
        # avoiding sql injection attack chances to protect the data from the users 
        sql_answer = c.execute(
                        'SELECT * FROM users WHERE username = :uname AND password = :pw;',
                        { 'uname': email, 'pw': password },
                        )
        
        if sql_answer == None :
                print(" your user_name or password is incorrect! please try again  ")
                answer = input("if you want to try again enter y or register enter r")
                if answer == 'y' :
                    main_function()
                    # allowing user to register 
                elif answer == 'r' :
                    if email_unique(sqlite3, connection.connector) == True :
                        name = input("Enter your Name : ")
                        phone = int(input("Enter yout phone No: "))
                        pwd = input("PASSWORD ")
                        c.execute(''' INSERT INTO members VALUES (?,?,?)''',(name,phone,pwd))    
                        connection.commit()     
                        return 'registered'       
                        
        else :
                print(" your are successfully login")
                return 'yes'

        
                
                
                