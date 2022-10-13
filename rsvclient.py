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

    
# 



























# parser = argparse.ArgumentParser(description='Calls on the function')
# parser.add_argument('function_string', type=str, help='Function Selection')
# parser.add_argument('--list', type=json.loads, help='Server Name')
# args = parser.parse_args()
# print(args.function_string)
# print(args.server_name)

# rsvclient list <server_name>
# rsvclient reserve <server_name> <seat_class> <passenger_name> <seat_number>
# rsvclient passengerlist <servername>                https://chase-seibert.github.io/blog/2014/03/21/python-multilevel-argparse.html

# py rsvclient.py reserve rsvserver FirstClass Alex 13
# py rsvclient.py list rsvserver
# https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse