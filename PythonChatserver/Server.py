from socket import *
import sys
import os
import os.path
#import thread  
import threading
from threading import Thread
from Client import Client
from Chatroom import Chatroom
from Parse import *

#C:\Python34\python.exe "C:\Users\evakn\Documents\CS4400 Internet Applications\HERE\CS4400\PythonChatserver\Server.py"

chatrooms={}
clients={}
#host=0.0.0.0
port = sys.argv[1]
max_conn = 5

def run():
	
	myip= "134.226.44.50" #should be reading the ip of the machine ist run on
	#myip=gethostbyname('localhost') 
	print(myip)
	
	#SETUP
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serverSocket.bind((myip, port))
	
	#WAIT FOR CONNECTION
	print( 'The server is ready to listen \n')	  
	serverSocket.listen(max_conn)
	
	try:
#ACCEPT CONNECTION
		conn, addr = serverSocket.accept() #acept connection from browser
		while True:			  
			#START THREAD FOR CONNECTION
			#start_new_thread(newClient,(conn, addr)) #start thread
			threading.Thread(target=newClient, args=(conn, addr)).start()
		
	except Exception as e:
		if serverSocket:
			serverSocket.close()
			print "Could not open socket:", message
		sys.exit(1) 
	
	#CLOSE CONNECTION 
	serverSocket.close()



def newClient(conn,addr):

	client=Client(0,0,0,0) #empty client object
		
	while True:
		try:
			msg=conn.recv(1250).decode()
			
			print(msg)
			if (msg): #if there is a message in the buffer decide what to do with it
			
				if checkHelo(msg): #helo
					sendHelo(ip, port, conn)
					
				elif checkKill(msg):#kill
					sys.exit(1)
					
				elif checkJoin(msg): #join
					if (client.join_ID==0): #if client has been not been initalised
						client=addClient(msg, conn, addr)
					joinRoom(msg, client)#joinroom
					
				elif checkExit(msg): #message is exit room
					removeClient(msg, conn, addr)
				elif checkDisconnect(msg):#message is disconnect  #TODO:Disconnect
					client=parseDisconnect(msg)
					del client
					serverSocket.close()
				elif checkMessage(msg):#message is message
					broadcastmessage(msg,conn)
					
				elif (checkError(msg) !=0): #TODO make up some errors (do we get a list?)
					sendError(conn, checkError(msg))#error description
					

		except Exception as e:
		#	print(e.with_traceback())
			break

	conn.close()
	

	
def addClient(msg, conn, addr):
	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)
	#create new client obj
	joinID= getID(clientName)	
	newClient= Client(clientName, conn, addr, joinID)
	clients[joinID]=newClient #ad client to client list
	return newClient

def joinRoom(msg, client): 
	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)
	roomID=getID(chatroomName)
	if (chatrooms[roomID]==""): #if chatroom doesnt exist yet
		chatroom = Chatroom(chatroomName, roomID)
		chatrooms[roomID]=chatroom
	chatroom.addclient(client)
	
	
def removeClient(msg, conn, addr):
	roomID, joinID, clientName= parseExit(msg)
	chatroom=chatrooms[roomID]
	client=clients[joinID]
	chatrooms.removeclient(client)
	sendExit(conn, chatroom, client)
	
def broadcastmessage(msg,conn):
	roomID, joinID, clientName, message=parseMessage(msg)
	client=clients[joinID]
	chatroom=chatrooms[roomID]
	sendMessage(conn,chatroom, msg)
			
def getID(name):
	id=0
	for i in name:
		temp=temp+ (int(name[i])^i)
		
	id= temp%1000
	return id
	

if __name__ == "__main__":
	run()
	
	

	