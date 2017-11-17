from socket import *
import sys
import os
import os.path
from thread import *


def main():
        chatroomname= "room 1"
        myname= "Eva"
	port = 8000
	host = localhost
	data=(chatroomname, host, port, myname)
	try:
		#SETUP AND CONNECT
		clientSocket = socket(AF_INET,SOCK_STREAM)
		clientSocket.connect(host, port)

	except error, (value, message):
		if clientSocket:
			clientSocket.close()
	       	print "Could not open socket:", message
	  	sys.exit(1)
	#clientSocket.send("JOIN_CHATROOM: ", chatroomname)
	#clientSocket.send(" CLIENT_IP: ", host)
	#clientSocket.send(" PORT: ",port)
	#clientSocket.send(" CLIENT_NAME: ", myname)
	clientSocket.send(data)
		)
	
	#CLOSE CONNECTION 
	clientSocket.close()
