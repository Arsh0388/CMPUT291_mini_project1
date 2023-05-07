
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
        lcode_locations = list(map(input("enter the location_codes for source and dstination ")))
       
        # asking whether they want to   put any cno or not 
     
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
            
        # c.execute(''' SELECT * FROM locations WHERE LOWER(?) = lcode ''', (lcode_locations[0]))
        # code_find = c.fetchone()
        # if code_find != None : 
        #     print("lcode is a location code ")
        # else :  
        #     selected_locations = []
        #     for i in range(len(lcode_locations)) : 
        #         if i == 0 : 
        #             print("Searching for source ")
        #         elif i == 1 :
        #             print("Searching the destination ")
        #         else :
        #             print("Searching for the enroute ")
                
        #         c.execute("SELECT * FROM locations WHERE LOWER(city) LIKE '%' || ? || '%' OR LOWER(prov) LIKE '%' || ? || '%' OR LOWER(address) LIKE '%' || ? || '%'", (lcode_locations[i],lcode_locations[i],lcode_locations[i]))
        #         matches = c.fetchall()  
        #         if len(matches) > 0 : 
        #             break_for_matches = False
        #             print("finding matches for the source and destination location ")
        #             for i in range(len(matches)) :
        #                 if i == 5 :
        #                     break_for_matches = input("if you want to see more lcoations enter True")
        #                     if  break_for_matches == False:
        #                         break
                            
        #                     else : 
        #                         print(" %s ", matches[i])
        #                 else : 
        #                     print(" %s ", matches[i])
                
        #         location_number = int(input(" Enter the location that you want to select in number  "))
        #         selected_locations.append(matches[location_number])
        # rno = c.lastrowid
        
        # car_ask = input("enter True if you want to enter any car number")
        # if car_ask : 
        #     cno = input("Enter the car number: ")
        #     if car_number_find(cno) : 
        #         c.execute("INSERT INTO rides(rno,price, rdate, seats, lugDesc, src, dst, driver, cno) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", (rno,price_per_seat, date, seats, luggae_description, source, destination, email, cno))
        
        # print("Ride successfully added with ride number:", rno)

def car_number_find(car_number) -> bool():
    c.execute(''' SELECT *
              FROM members M, cars C
              WHERE cno = ?''', car_number)
    
    if c.fetchone() != None :
        return True  
    return False     
        
        
        

        
        
