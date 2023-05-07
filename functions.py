import sqlite3
import login 
import unseen
ride_no = 0
connection = sqlite3.connect("./sql.db")
c = connection.cursor()
def message_display() :
    login_asnwer = login.main_function()
    unseen.unseen_message_display()
    
def offer_ride() :
    option = input("type y if you want to offer a ride")
    if option == 'y' :
        date,seats,price_per_seat, luggae_description, source, destination = input("enter the details of the ride lie \n date,seats,price_per_seat, luggae_description, source, destination \n please enter the luggage_desciption in quotes ' ' like this ")
        seats = int(seats)
        price_per_seat = int(price_per_seat)
        repond = input("type yes if you want to enter the option of adding a car option , and any set of enroute locations")
        lcode_locations = list(map(input("enter the location_codes for source dstination and enroute ")))
        
        c.execute(''' SELECT * FROM locations WHERE LOWER(?) = lcode ''', (lcode_locations))
        code_find = c.fetchone()
        if code_find != None : 
            print("lcode is a location code ")
        else :  
            c.execute("SELECT * FROM locations WHERE LOWER(city) LIKE '%' || ? || '%' OR LOWER(prov) LIKE '%' || ? || '%' OR LOWER(address) LIKE '%' || ? || '%'", (src_kw, src_kw, src_kw))
            matches = c.fetchall()  
            if len(matches) > 0 : 
                break_for_matches = False
                print("finding matches for the source and destination location ")
                for i in range(len(matches)) :
                    if i == 5 :
                        break_for_matches = input("if you want to see more lcoations enter True")
                        if  break_for_matches == False:
                            break
                        
                        else : 
                            print(" %s ", matches[i])
                    else : 
                        print(" %s ", matches[i])


def car_number_find(car_number) :
    c.execute(''' SELECT M.name 
              FROM members M, cars C
              WHERE cno = ? AND M.name = C.owner''', car_number)
    
    member = c.fetchone()
    if member != None :
        
        c.execute(''' UPDATE TABLE rides 
                  SET rno = ? AND driver = ? 
                  WHERE cno = ? ''',(ride_no,member,car_number))
        
        
        
