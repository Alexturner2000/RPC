from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
# Restrict to a particular path.


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(
    ("localhost", 9999), requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()


class flight:
    def __init__(self, passengerClass, passengerName, passengerSeat):
        self.passengerClass = passengerClass
        self.passengerName = passengerName
        self.passengerSeat = passengerSeat


c1 = flight("economy", "Leon", "1")
c3 = flight("economy", "Alex", "3")
c23 = flight("business", "Nate", "23")

# Reserve
def reserve_function(function_name, passenger_class, passenger_name, passenger_seat):
    return(" Successfully reserved seat " + passenger_seat + " for passenger " + passenger_name)
    # return(" Failed to reserve: invalid seat number")
    # return(" Failed to reserve: seat not available")
server.register_function(reserve_function, 'reserve_function')

# List
def list_function(function_name):
    return(c1.passengerClass)
    
server.register_function(list_function, 'list_function')

# Passenger List
def passengerlist_function(function_name):
    return(" PASS LISTING")
server.register_function(passengerlist_function, 'passengerlist_function')







server.serve_forever() # Endless server loop

