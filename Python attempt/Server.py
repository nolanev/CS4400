from socket import *
import sys
import os
import os.path
from thread import *

def main():
	port = 8000
	max_conn = 5
	
	try:
		#SETUP
		serverSocket = socket(AF_INET,SOCK_STREAM)
		serverSocket.allow_reuse_address=True
		serverSocket.serve_forever()
		
		#WAIT FOR CONNECTION
		print( 'The server is ready to listen \n')	  
		serverSocket.listen(max_conn)

	#except error, (value, message):
	#	if serverSocket:
	#		serverSocket.close()
	 #      	print "Could not open socket:", message
	  #	sys.exit(1) 

	while True:
                #ACCEPT CONNECTION
                conn, addr = serverSocket.accept() #acept connection from browser

                                
                data = conn.recv(chatroomname, chost, cport, cname)# recieve join request
                               

                                #START THREAD FOR CONNECTION
                start_new_thread(new_client,(conn, data, addr)) #start thread
			
	#CLOSE CONNECTION 
	serverSocket.close()

def new_client(conn,data,addr):

        reply=(chatroomname,conn,addr,ref,joinid)
        conn.send(reply)        
                         
        #JOINED_CHATROOM: [chatroom name]
        #SERVER_IP: [IP address of chat room]
        #PORT: [port number of chat room]
        #ROOM_REF: [integer that uniquely identifies chat room on server]
        #JOIN_ID: [integer that uniquely identifies client joining

        #todo send message to chatroom

        joinid=joinid+1#update join id for next request
