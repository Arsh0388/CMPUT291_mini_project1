
import sqlite3
import login 
import unseen
ride_no = 0
connection = sqlite3.connect("./sql.db")
c = connection.cursor()

# this is going to be the very first task after login i.e updating the messages. 
def message_display() :
    login_asnwer = login.main_function()
    unseen.unseen_message_display()
    
# this is a first major task of the project of offering a ride 

def offer_ride() :
    option = input("type y if you want to offer a ride")
    if option == 'y' :
        date,seats,price_per_seat, luggae_description, source, destination = input("enter the details of the ride lie \n date,seats,price_per_seat, luggae_description, source, destination \n please enter the luggage_desciption in quotes ' ' like this ")
        seats = int(seats)
        price_per_seat = int(price_per_seat)
        lcode_locations = list(map(input("enter the location_codes for source and dstination ")))
       
        # asking whether they want to   put any car_number or not 
        
        rno = c.lastrowid
        condition = True
        while condition : 
            car_question = input("Enter yes if you want add any car nno")
            if car_question == 'yes' :
                cno = input("Enter the car no: ")
                if car_number_find(cno) :
                    condition = False
            else : 
                condition = False  
                
        #asking enroute information 
        
        enroute_question = input("Type yes if you want to enter any enroute information/ lcode: ")
        if enroute_question == 'yes' :
            enroute_lcode = input("Enter the enroute lcode: ")
            enroute_location = lcode_locations(enroute_lcode)
            # adding enroute information into he table enroute 
            c.execute(''' INSERT INTO enroute VALUES(?,?)''',rno,enroute_location[3]) 
            
            
        # for source 
        source_location = lcode_locations(source)
        destination_location = lcode_locations(destination).   # for destination 
        rno = c.lastrowid.  # rideno which is the primary key for the table rides 
        
        # email part is nor clear in the project -- have ot check whether it is mandatory to enter or not 
        if cno != 0 : 
            email = car_owner_email(cno)
            c.execute("INSERT INTO rides(rno,price, rdate, seats, lugDesc, src, dst, driver, cno) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", (rno,price_per_seat, date, seats, luggae_description, source_location, destination_location, email, cno))
        # confirming whether 
        else : 
            c.execute("INSERT INTO rides(rno,price, rdate, seats, lugDesc, src, dst) VALUES (?,?, ?, ?, ?, ?, ?)", (rno,price_per_seat, date, seats, luggae_description, source_location, destination_location))    
        print("Ride successfully added with ride number:", rno)

# checking whether the car_number enetered is valid or not !! 
def car_number_find(car_number) -> bool():
    c.execute(''' SELECT *
              FROM members M, cars C
              WHERE cno = ?''', car_number)
    
    if c.fetchone() != None :
        return True  
    return False    

# finding the details of the car owner
def car_owner_email(car_number) :
    c.execute(''' SELECT M.email
              FROM members M, cars C
              WHERE cno = ?''', (car_number))
    return c.fetchone()

# functiont that finds whether its a lcode or is there any city with the similar lcode or charachters 
# this is a general function that is determining whether the entered text is a lcode if not then its is finidng similar cities with text 

def lcode_locations(lcode) : 
        c.execute(''' SELECT * FROM locations WHERE LOWER(?) = lcode ''', (lcode))
        code_find = c.fetchone()
        if code_find != None : 
            print("lcode is a location code ")
        else :  
            c.execute("SELECT * FROM locations WHERE LOWER(city) LIKE '%' || ? || '%' OR LOWER(prov) LIKE '%' || ? || '%' OR LOWER(address) LIKE '%' || ? || '%'", (lcode,lcode,lcode))
            matches = c.fetchall()  
            if len(matches) > 0 : 
                print("finding matches: ")
                for i in range(len(matches)) :
                    if i == 5 :
                        break_for_matches = input("if you want to see more lcoations enter True")
                        if  break_for_matches == False:
                            break
                            
                        else : 
                            print(" %s ", matches[i])
                    else : 
                        print(" %s ", matches[i])
                
                location_number = int(input(" Enter the location that you want to select in number  "))
                selected_location = matches[location_number][3]
        return selected_location
        

        
