
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
        destination_location = lcode_locations(destination)
        rno = c.lastrowid
        
        # email part is nor clear in the project -- 
        if cno != 0 : 
            email = car_owner_email(cno)
            c.execute("INSERT INTO rides(rno,price, rdate, seats, lugDesc, src, dst, driver, cno) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", (rno,price_per_seat, date, seats, luggae_description, source_location, destination_location, email, cno))

        else : 
            c.execute("INSERT INTO rides(rno,price, rdate, seats, lugDesc, src, dst) VALUES (?,?, ?, ?, ?, ?, ?)", (rno,price_per_seat, date, seats, luggae_description, source_location, destination_location))    
        print("Ride successfully added with ride number:", rno)

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
        

def search_ride(location):
    location_split = location.strip().split()
    rides_list = []
    for i in range(len(location_split)):
        c.execute('''SELECT rno, cno FROM rides, enroute
                     WHERE rides.rno = enroute.rno AND
                     (LOWER(src) LIKE '%' || ? || '%' OR
                     LOWER(dst) LIKE '%' || ? || '%' OR
                     LOWER(enroute) LIKE '%' || ? || '%')
                     UNION
                     SELECT rno, cno FROM rides, locations
                     WHERE rides.src = locations.lcode AND
                     (LOWER(city) LIKE '%' || ? || '%' OR
                     LOWER(prov) LIKE '%' || ? || '%' OR
                     LOWER(address) LIKE '%' || ? || '%')''',
                  (location_split[i], location_split[i], location_split[i],
                   location_split[i], location_split[i], location_split[i]))
        matches = c.fetchall()
        rides_information = []
        for match in matches:
            c.execute('''SELECT * FROM rides, cars
                         WHERE cars.cno = rides.cno AND rides.rno = ?''', (match[0],))
            rides_information.extend(c.fetchall())
        rides_list.extend(rides_information)
    for k in range(len(rides_list)):
        if k > 4:
            more_rides = input("Type 'yes' if you want to see more than 5 rides: ")
            if more_rides != 'yes':
                break
        print(rides_list[k])
    selected_ride_number = int(input("Enter the selected ride number: "))
    return rides_list[selected_ride_number]

def message_sending(ride_number):
    message_for_rider = input("Enter the message that you want to give to owner/rider: ")
    c.execute('''UPDATE inbox 
                 SET content = ? 
                 WHERE rno = ?''', (message_for_rider, ride_number))


    
def post_request() :
    date, p_lcode, d_lcode , amount_per_seat = map(list(input("Enter the date,  pickup location_code, drop_off location code, amount per seat")))
    date = date(date)
    amount_per_seat = int(amount_per_seat)
    email = input("Enter the email address of the member: ")
    c.execute(''' SELECT email FROM member 
                    WHERE email = ? ''', (email))
    rid = c.lastrowid
    confirmation =c.fetchone() 

    if email == confirmation : 
        c.execute(''' INSERT INTO TABLE  requests VALUES (?, ?, ?, ?, ?, ?)''',(rid, email, date,p_lcode,d_lcode,amount_per_seat))
    

def delete_requests() :
    email = input(" Enter your email address: ")
    c.execute(''' SELECT * FROM requests
                WHERE email = ? ''',(email))
    requests = c.fetchall()
    lcode
    for i in range(len(requests)) :
        print(f' {i}. {requests[i]} ')
        if len(requests) >= 5 : 
            user_prompt = input("Ente y if you want to see more requests else enter anyother keyword if you want to search for any ride requests ")
            if user_prompt == 'y' : 
                continue
            else : 
                lcode = user_prompt
                break 
     
    c.execute(''' SELECT * FROM requests R, locations L
                  WHERE R.lcode = L.lcode 
                  AND R.lcode = ? OR L.city = ?''',(lcode,lcode))
    final_result = c.fetchall()
    for i in range(len(final_result)) : 
        print(" %i.  %s ",i,final_result[i])
        if i % 5 == 0 :
            ask = input("Enter y to see more results ")
            if ask == 'y' : 
                continue 
            else : 
                break
 # left with the ;ast line in t his part 5th figuring out the part " select a request and message the posting member"        
def bookings(email,rno) :
    
    # making bookings and cancelling it. 
    
    
# arsh code  not corrected by chatgpt everything same except ht ematched statement for i am trying to use a aquery and it used loop
# it extended the rids_list list for better 


# def search_ride(location) :
#     location_split = location.strip(' ')
#     rides_list = []
#     for i in range(len(location_split)) :
#         # matching for the rides and showing the results for the customer 
        
#         c.execute(''' SELECT rno , cno FROM rides,enroute  WHERE rides.rno = enroute.rno AND 
#                   LOWER(src) LIKE '%' || ? || '%' 
#                   OR LOWER(dst) LIKE '%' || ? || '%' 
#                   OR LOWER(enroute) LIKE  '%' || ? || '%' 
#                   UNION 
#                   SELECT * FROM locations WHERE LOWER(city) LIKE '%' || ? || '%' 
#                   OR LOWER(prov) LIKE '%' || ? || '%' 
#                   OR LOWER(address) LIKE '%' || ? || '%' ''',
#                   (location_split[i],location_split[i],location_split[i],location_split[i],location_split[i],location_split[i]))
#         matches = c.fetchall()
        
#         # stackoverflow help in putting list inside the query for python 
#         matches = tuple(matches)
#         c.execute(''' SELECT * FROM rides, cars 
#                   WHERE cars.cno = rides.cno    
#                   AND rides.rno in {}
#                   '''.format(matches))
#         rides_information = c.fetchall()
#     for k in range(len(rides_information)) :

#         if k > 4 :
#             more_rides = input("Type yes if you want to see more than 5 rides ")
#             if more_rides == 'yes' :
#                 continue
#             else : 
#                 break
#         else : 
#             print(" %s ",rides_information[k])
    
#     selected_ride_number = int(input(" Enter the selected ride number : "))
#     return rides_information[selected_ride_number]

# def message_sending(ride_number) :
#     message_for_rider = input("Enter the message that you want to give to owner / rider ")
    
#     c.execute(''' UPDATE TABLE inbox 
#               SET content = ? 
#               WHERE rno = ? ''', (message_for_rider,ride_number))
