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

def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# initialize socket
        s.bind(('', listening_port))
        s.listen(max_conn)
        print "[*] initializing sockets ...Done"
        print "[*] Sockets binded successfully..."
        print ("[*] Server strated [ %d ]\n" % (listening_port))
    exception, e:
	print "[*] Unble to initialize socket"
	sys.exit(2)

    while 1:
	try:
	    conn, addr = s.accept()
	    data = conn.recv(buffer_size)
	    start_new_thread(conn_string, (conn, data, addr))
	except KeyboardInterupt:
	    s.close()
	    print "\n[*] Proxy server shutting down ..."
	    print "[*] Nothing more buddy..."
	    sys.exit(1)
    s.close()

def conn_string(conn, data, addr):
    #client browser request appears here
    try:
	first_line = data.split('\n')[0]
	url = first_line.split(' ')[1]
	htt_pos = url.find("://")
	if (http_pos == -1):
	    temp  url
	else:
	    temp = url[(http_pos+3):] #get the rest of the url
	port_pos = temp.find(":") #find the ps of the port
	webserver_pos = temp.find("/") #find te end of the webserver
	if webserver_pos == -1:
	    webserver_pos = len(temp)
	webserver = ""
	port = -1
	if (port_pos == -1 or webserver_pos < port_pos):
	    port = 80
	    webserver = temp[:webserver_pos]
	else:
	    #specific port
	    port = nt((temp[(port_pos+1):])[:webserver_pos -port_pos-1])
	    webserver = temp[:port_pos]
	proxy_server(webserver, port, conn, addr, data)
    except Exeception, e:
	print (e)
