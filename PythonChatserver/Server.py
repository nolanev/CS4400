from socket import *
import sys
import os
import os.path
from thread import *

joinID=0
roomID=0

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
                conn, addr = serverSocket.accept() #acept connection from browser
				  
                #START THREAD FOR CONNECTION
                start_new_thread(newClient,(conn, addr)) #start thread
			
	except error, (value, message):
		if serverSocket:
			serverSocket.close()
	       	print "Could not open socket:", message
	  	sys.exit(1) 

	
	#CLOSE CONNECTION 
	serverSocket.close()

def newClient(conn,addr):

    while True:
		try:
			msg=conn.recv(BUFFERSIZE).decode()
			if msg #if there is a message in the buffer decide what to do with it
				
					if #message is join
					#add_client
					elif #message is leav
					#remove Client
					elif #message id disconnect
					#close socket
					

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
	
def addClient(msg, conn, addr):

	#parse to find client name
	clientName = parse(msg)
		
	#create new client obj
	newClient= Client(clientName, conn, addr, joinId)
	joinID++ #join id for next client
	return newClient

def joinRoom(msg, client):
	roomName= parse(msg)	
	#chatroom =Chatroom(roomName, roomID) that would be craeting a new chatroom
	client.roomID=roomID
	#creat room id
	if !chatrooms[roomid]:
		#error
	else:
		chatroom.addClient(client)
		roomID++ #create new roomid
	
def removeClient(msg, conn, addr):
	#remvoe client from room
	#parse
	#delete
	fo
	
	
	
if __name__ == "__main__":
    run()
