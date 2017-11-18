from socket import *
import sys
import os
import os.path
from thread import *

joinID=0
roomID=0
chatrooms[]
clients[]

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

	client= new Client
	client=NULL #empty client is this being initialised correctly
	
    while True:
		try:
			msg=conn.recv(BUFFERSIZE).decode()
			if msg #if there is a message in the buffer decide what to do with it
				if checkHelo(msg): #helo
					sendHelo(ip, port,conn)
				elif checkKill(msg):#kill
					sys.exit(1)
				elif checkJoin(msg): #join
					if (client=NULL):
						client=addClient(msg, conn, addr)
					joinRoom(msg, client)#joinroom
				elif checkExit(msg): #message is exit room
					removeClient(msg, conn, addr)
				elif checkDisconnect(msg):#message is disconnect  #TODO:Disconnect
					#delete client
					#close socket
				elif checkMessage(msg):#message is message
					sendMessage(conn,)#broadcast
				elif (checkError(msg) !=0): #TODO make up some errors (do we get a list?)
					sendError(conn, checkError(msg))#error description
					

        except Exception as e:
            print(e.with_traceback())
            break

	conn.close()
	

	
def addClient(msg, conn, addr):
	#parse to find client name
	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)
		
	#create new client obj
	joinID= getID(clientName)
	newClient= Client(clientName, conn, addr, joinID)
	clients[joinID]=newClient #may move this
	#joinID++ #join id for next client
	return newClient

def joinRoom(msg, client): #TODO: Look at how Im making roomid
	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)
	#need to be able to check room id from name here
	#derive roomid from name?
	roomID=getID(chatroomName)
	if !chatrooms[roomID]: #if chatroom doesnt exist yet
		chatroom = new Chatroom(chatroomName, roomID)
		chatrooms[roomID]=chatroom
	chatroom.addClient(client)
	roomID++ #create new roomid
	
def removeClient(msg, conn, addr):
	roomRef, joinID, clientName parseExit(msg)
	chatrooms[roomref]=chatroom
	clients[joinID]=client
	chatrooms.removeClient(client)
	client.joinID=0
	sendExit(conn, chatroom, client)
		
def getID(name):
	id=0
	for (in in lengthof(name)):
		temp=temp+ (int(name[i])^i)
		
	id= temp%1000
	return id
	
if __name__ == "__main__":
    run()