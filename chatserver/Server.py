from socket import *
import sys
import os
import os.path
from thread import *

class Client:


def run():
	port = 8000
	max_conn = 5
	jid=0
	
		#SETUP
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.allow_reuse_address=True
	serverSocket.serve_forever()
	
	
	#WAIT FOR CONNECTION
	print( 'The server is ready to listen \n')	  
	serverSocket.listen(max_conn)
	
	

	
	while True:
                #ACCEPT CONNECTION
                Clientconn, Clientaddr = serverSocket.accept() #acept connection from browser
				
                                
                #data = conn.recv(chatroomname, chost, cport, cname)# recieve join request
                               

                #START THREAD FOR CONNECTION
                start_new_thread(new_client,(Clientconn, Clientaddr)) #start thread
			
	except error, (value, message):
		if serverSocket:
			serverSocket.close()
	       	print "Could not open socket:", message
	  	sys.exit(1) 

	
	#CLOSE CONNECTION 
	serverSocket.close()

def new_client(conn,addr):

    while True:
		try:
			msg=conn.recv(BUFFERSIZE).decode()
			if msg #if there is a message in the buffer
				
					if #message is join
					
					elif #message is leav
					
					elif #message id disconnect
		

        except Exception as e:
            print(e.with_traceback())
            break

		
                         
        #JOINED_CHATROOM: [chatroom name]
        #SERVER_IP: [IP address of chat room]
        #PORT: [port number of chat room]
        #ROOM_REF: [integer that uniquely identifies chat room on server]
        #JOIN_ID: [integer that uniquely identifies client joining

        #todo send message to chatroom

    conn.close()
	
def add_Client(msg, conn, addr)
	#parse message
	joinId=jid
	jid =jid +1
	new_client= Client(clientName, conn, addr, joinId)
	
	#send message to chatroom
	#clientSocket.send("JOIN_CHATROOM: ", chatroomname)
	#clientSocket.send(" CLIENT_IP: ", host)
	#clientSocket.send(" PORT: ",port)
	#clientSocket.send(" CLIENT_NAME: ", myname)
	
