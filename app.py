import socket, sys
from thread import *


try:
    listening_port = int(raw_input("[*] Enter listening port number: "))
except KeyboardInterrupt:
    print "\n[*] User Interrupted"
    print "[*] application exiting ..."
    sys.exit()

max_conn = 5 # Max connection queues to hold
buffer_size = 8192 # Max socket buffer size

