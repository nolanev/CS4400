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
	ip= #my ip
	
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
	#here is where I should crete my client obj?
    while True:
		try:
			msg=conn.recv(BUFFERSIZE).decode()
			if msg #if there is a message in the buffer decide what to do with it
					if parseHelo(msg) #helo
						sendHelo(ip, port,conn)
					elif parseKill(msg)#kill
						sys.exit(1)
					elif parseJoin(msg)#message is join
						if #client is new
							addClient(msg, conn, addr
							#add client
						joinRoom(msg, client)#joinroom
					elif parseExit(msg) #message is exit room
						removeClient(msg, conn, addr)
					elif parseDisconnect(msg)#message is disconnect
						#delete client
						#close socket
					elif parseMessage(msg)#message is message
						sendMessage(conn,chatroom)#broadcast
					else 
						sendError(conn, parseError(msg))#error description
					

        except Exception as e:
            print(e.with_traceback())
            break

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
	#sendExit(conn, chatroom, client)
	#parse
	#delete
	fo
	
def boradcast(msg):
	
	
if __name__ == "__main__":
    run()