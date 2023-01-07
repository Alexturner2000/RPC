import xmlrpc.client
import argparse

proxy = xmlrpc.client.ServerProxy("http://localhost:9999")

while True:
    function_name = input(" Function : ")
    
    if function_name == "reserve":
        server_name = input(" Server Name : ")
        passenger_class = input(" Class : ")
        passenger_name = input(" Name : ")
        passenger_seat = input(" Seat Number : ")
        print(proxy.reserve_function(function_name, passenger_class, passenger_name, passenger_seat) + "\n")

    if function_name == "list":
        server_name = input(" Server Name : ")
        print(proxy.list_function(function_name))
        
    if function_name == "passengerlist":
        server_name = input(" Server Name : ")
        print(function_name)
        print(server_name)
        # proxy.passengerlist_function(variables)

    if function_name not in ["reserve", "list", "passengerlist"]:
        print(" Function does not exist\n")
