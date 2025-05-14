import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  conn.root.exposed_append(5)       # Call an exposed operation,
  conn.root.exposed_append(6)       # and append two elements
  conn.root.exposed_append(11)
  conn.root.exposed_append(9)
  print (conn.root.exposed_value())   # Print the result
  print(conn.exposed_sum())
  print(conn.exposed_showElement(2))
