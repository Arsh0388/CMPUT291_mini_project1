import sqlite3
import login 
import unseen
 
connection = sqlite3.connect("./sql.db")
c = connection.cursor()
def message_display() :
    login_asnwer = login.main_function()
    unseen.unseen_message_display()
    
def offer_ride() :
    option = input("type y if you want to offer a ride")
    if option == 'y' :
        date,seats,price_per_seat, luggae_description, source, destination = input("enter the details of the ride lie \n date,seats,price_per_seat, luggae_description, source, destination \n please enter the luggage_desciption in quotes ' ' like this ")
        repond = input("type yes if you want to enter the option of adding a car option , and any set of enroute locations")
        lcode_locations = list(map(input("enter the location_codes for source dstination and enroute ")))
        
