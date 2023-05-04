import csv
import sqlite3
import pandas as pd
from sqlalchemy import types


# reference -- stackoverflow for a conveniant way to populate the database and avoiding duplicacy in the code 

#  making a Proper conneciton with the data base to setup the login page 
def connection() :
    global  cursor_1
    connection = sqlite3.connect('./sql.db')
    cursor_1 = connection.cursor()
    
    cursor_1.execute('PRAGMA foreign_keys=ON;')
    
    creating_table = '''CREATE TABLE IF NOT EXISTS "members" ("email" TEXT, " name" TEXT, "phone" INTEGER, "pwd" TEXT,PRIMARY KEY("email"));
                        CREATE TABLE IF NOT EXISTS "cars" ("cno" TEXT, "make" TEXT, "model" TEXT, "year" YEAR, "seats" INTEGER, "owner" TEXT, PRIMARY KEY("cno"));
                        CREATE TABLE IF NOT EXISTS "locations" ("lcode" TEXT , "city" TEXT, "prov" TEXT, "address" TEXT, PRIMARY KEY ("lcode"));
                        CREATE TABLE IF NOT EXISTS "rides" ("rno" INTEGER, "price" INTEGER, "rdate" DATE, "seats" INTEGER, "lugDesc" TEXT, "src" TEXT, "dst" INTEGER, "driver" TEXT, "cno" INTEGER, PRIMARY KEY ("rno"), FOREIGN KEY ("cno") REFERENCES "cars")
                        CREATE TABLE IF NOT EXISTS "bookings" ("bno" INTEGER, "email" TEXT, "rno" INTEGER, "cost" INTEGER, "seats" INTEGER, "pickup" TEXT, "dropoff" TEXT, FOREIGN KEY("email") REFERENCES "members",FOREIGN KEY("rno") REFERENCES "rides" )
                        CREATE TABLE IF NOT EXISTS "enroute" ("rno" INTEGER, "lcode" TEXT, PRIMARY KEY("rno", "lcode"), FOREIGN KEY ("rno") REFERENCES "rides", FOREIGN KEY ("lcode") REFERENCES "locations");
                        CREATE TABLE IF NOT EXISTS "requests" ("rid" INTEGER, "email" TEXT, "rdate" DATE, "pickup" TEXT, "dropoff" TEXT, "amount" INTEGER, PRIMARY KEY ("rid"), FOREIGN KEY ("email") REFERENCES "member" );
                        CREATE TABLE IF NOT EXISTS "inbox" ("email" TEXT, "msgTimestamp" TIMESTAMP, "sender" TEXT, "content" TEXT, "rno" INTEGER, "seen" TEXT, PRIMARY KEY ("email") REFERNCES "members", FOREIGN KEY ("email") REFERENCES "members", FOREIGN KEY ("rno") REFERENCES "rides" );
                        
    '''
    
    cursor_1.executescript(creating_table)

# using pandas libarary to populate the database and tables 

def populating_table(table,filename) :

    df = pd.read_csv(filename,sep=',',quotechar='\'',encoding='utf8')
    df.to_sql(table,con=connection,index=False,if_exists='append')

def main() :
    
    # populating tables by calling the function populating_table and passing general inputs  
    populating_table("members","members.csv")
    populating_table("cars","cars.csv")
    populating_table("locations","locations.csv")
    populating_table("rides","rides.csv")
    populating_table("bookings","bookings.csv")
    populating_table("enroute","enroute.csv")
    populating_table("requests","requests.csv")
    populating_table("inbox","inbox.csv")
    