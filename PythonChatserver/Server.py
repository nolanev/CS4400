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
clients={} #dictionaries of chatroom and client objcets with their ID number as a key
#host=0.0.0.0
port = int(sys.argv[1])
max_conn = 5

def run():
	
	#myip= "134.226.44.50" #should be reading the ip of the machine ist run on
	#myip=gethostbyname('localhost') 
	#print(myip)
	
	#SETUP
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serverSocket.bind((gethostbyname(gethostname()), port))
	ip=(gethostbyname(gethostname()))
	#print(ip)
	
	#WAIT FOR CONNECTION
	print( 'The server is ready to listen \n')	  
	serverSocket.listen(max_conn)
	
	while True:	
	
#ACCEPT CONNECTION
		try:
				  
			#START THREAD FOR CONNECTION
			conn, addr = serverSocket.accept() #acept connection from browser
			
			#start_new_thread(newClient,(conn, addr)) #start thread
			#print( 'Starting new thread \n')	
			threading.Thread(target=newClient, args=(conn, addr,ip,port)).start()
		
		except Exception as e:
			if serverSocket:
				serverSocket.close()
				#print "Could not open socket:", message
			sys.exit(1) 
	
	#CLOSE CONNECTION 
	serverSocket.close()



def newClient(conn,addr,ip,port):
	#print("started thread") printed indefinitly????
	client=Client(0,0,0,0) #empty client object
		
	while True:
		try:
			print("try")
			msg=conn.recv(1024).decode()
			print("RECIEVED: ")				
			print(msg)
			
			if (msg): #if there is a message in the buffer decide what to do with it
				
				if checkHelo(msg): #helo
					#print("helo returned true")
					sendHelo(conn,addr,ip,port)
					
				elif checkKill(msg):#kill
					sys.exit(1)
					
				elif checkJoin(msg): #join
					
					if (client.join_ID==0): #if client has been not been initalised
						client=addClient(msg, conn, addr)
					
					
					joinRoom(msg,conn, client,ip)#joinroom#
					
					print("yep")
					helloMsg ="CHAT: " #+ str(client.name)
					conn.sendall(helloMsg.encode())
					print("yep")
					
				elif checkExit(msg): #message is exit room
					removeClient(msg, conn, addr)
				elif checkDisconnect(msg):#message is disconnect  #TODO:Disconnect
					client=parseDisconnect(msg)
					#del client
					serverSocket.close()
				elif checkMessage(msg):#message is message
					broadcastmessage(msg,conn)
					
				elif (checkError(msg) !=0): #TODO make up some errors (do we get a list?)
					sendError(conn, checkError(msg))#error description
				else: print("giveup")	

		except Exception as e:
		#	print(e.with_traceback())
			break

	conn.close()
	

	
def addClient(msg, conn, addr): #passes test

	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)

	joinID= getID(clientName)	
		
	newClient= Client(clientName, conn, addr, joinID)

	clients[joinID]=newClient #ad client to client list
	#print(newClient.name)
	#print((clients[joinID]).name)
	#print(newClient.join_ID)
	
	return newClient

def joinRoom(msg, conn, client,ip): 
	chatroomName, clientIP, clientPort, clientName= parseJoin(msg)
	print
	roomID=getID(chatroomName)
	clientlist={}
	if roomID not in chatrooms: #if chatroom doesnt exist yet
	
		chatroom = Chatroom(chatroomName, roomID)
	
		chatrooms[roomID]=chatroom 		
		
	chatroom.addclient(client) 
		
	joinMsg = "JOINED_CHATROOM: " + str(chatroom.roomName) + "\nSERVER_IP: "+ str(ip) + "\nPORT: " + str(clientPort)+ "\nROOM_REF: " + str(roomID) + "\nJOIN_ID: " + str(roomID)  + "\n"
	
	print(joinMsg)	
	conn.sendall(joinMsg.encode())
	
	#sendJoin(conn, chatroom, client, clientIP, clientPort)
	#sendJoin(conn, chatroom, client, ip, port):
	
def removeClient(msg, conn, addr):
	roomID, joinID, clientName= parseExit(msg)
	chatroom=chatrooms[roomID] ###cant really do this
	client=clients[joinID]
	chatrooms.removeclient(client)
	sendExit(conn, chatroom, client)
	
	
def broadcastmessage(msg,conn):
	roomID, joinID, clientName, message=parseMessage(msg)
	client=clients[joinID]
	chatroom=chatrooms[roomID]
	sendMessage(conn,chatroom, msg)
			
def getID(name):
	idval=0
	temp=0
	for i in name:
		temp=temp+ ord(i)
	idval= temp%1000
	#print(idval)
	return idval
	

if __name__ == "__main__":
	run()
	
	

	
