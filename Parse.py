#throw io exception??
from Client import Client
from Chatroom import Chatroom
##########KILL##########
def	checkKill(msg):	
	if msg=="KILL_SERVICE\n":
		return True
	else: return False

##########HELO##########
def	checkHelo(msg):
	print("check helo")
	if msg=="HELO BASE_TEST\n":
		print("returning true")
		return True
	else: 
		print("returning false")
		return False
def sendHelo(conn, addr,ip,port):
	#"HELO text\nIP:[ip address]\nPort:[port number]\nStudentID:[your student ID]\n"
	HELOmsg = "HELO text \nIP: " + str(ip) + "\nPort: " + str(port) + "\nStudentID: 14335043"
	#HELOmsg=HELOmsg.encode()
	
	conn.sendall(HELOmsg.encode())
	

##########JOIN##########
def	checkJoin(msg):
	if match("JOIN_CHATROOM: (\w+\s*)+\nCLIENT_IP: (\d)\nPORT: (\d)\nCLIENT_NAME: (\w+\s*)+\n",msg):
		return True
	else: return False
def parseJoin(msg):
	splitMessage = msg.split('\n')
	#JOIN_CHATROOM: [chatroom name]
	chatroomName = splitMessage[0].split(':')[1].strip()
	#CLIENT_IP: [IP Address of client if UDP | 0 if TCP]
	clientIP =splitMessage[1].split(':')[1].strip()
	#PORT: [port number of client if UDP | 0 if TCP]
	clientPort=splitMessage[2].split(':')[1].strip()
	#CLIENT_NAME: [string Handle to identifier client user]
	#CLIENT_NAME: [string Handle to identifier client user]
	clientName = splitMessage[3].split(':')[1].strip()
	return chatroomName, clientIP, clientPort, clientName
def sendJoin(conn, chatroom, client, ip, port):
	joinMsg = "JOINED_CHATROOM: " + chatroom.roomName 
	+ "\nSERVER_IP: " + str(ip)
	+ "\nPORT: " +  str(port)
	+ "\nROOM_REF: " + chatroom.roomID
	+ "\nJOIN_ID: " + client.join_id
	conn.sendall(joinMsg.encode())

##########ERROR##########	
def	checkError(msg):
	if match("ERROR_CODE: (\d) +\n)",msg):
		errorcode= msg.split(':')[1].strip()
	else:
		return 0
	return errorCode
def sendError(conn, errorcode):
	errorMsg=''
	if errorcode ==1:
		errorMsg= "ERROR_DESCRIPTION: "
	conn.sendall(errorMsg.encode())

##########EXIT##########		
def	checkExit(msg):
	if match("LEAVE_CHATROOM: (\w+\s*)+\nJOIN_ID: (\d)+\nCLIENT_NAME: (\w+\s*)+\n",msg):
		return True
	else: return False	
def parseExit(msg):
	splitMessage = msg.split('\n')
	#LEAVE_CHATROOM: [ROOM_REF]
	roomRef= splitMessage[0].split(':')[1].strip()
	#JOIN_ID: [integer previously provided by server on join]
	joinID= splitMessage[1].split(':')[1].strip()
	#CLIENT_NAME: [string Handle to identifier client user]
	clientName= splitMessage[2].split(':')[1].strip()
	return roomRef, joinID, clientName
def sendExit(conn, chatroom, client):
	exitMsg= "#LEFT_CHATROOM: " +chatroom.roomID
	+ "\nJOIN_ID: " + client.join_id
	conn.sendall(exitMsg.encode())

##########DISCONNECT##########	
def	checkDisconnect(msg):
	if match("DISCONNECT: (\d) +\nPORT: (\d) +\nCLIENT_NAME: (\w+\s*)+\n",msg):
		return True
	else: return False
def parseDisconnect(msg):
	splitMessage = msg.split('\n')
	#DISCONNECT: [IP address of client if UDP | 0 if TCP]
	clientIP= splitMessage[0].split(':')[1].strip()
	#PORT: [port number of client it UDP | 0 id TCP]
	clientPort=splitMessage[1].split(':')[1].strip()
	#CLIENT_NAME: [string handle to identify client user]
	clientName=splitMessage[3].split(':')[1].strip()
	
	client=clients[joinID]
	return client
	


##########BROADCAST##########	
def	checkMessage(msg):
	if match("CHAT: (\d) +\nJOIN_ID: (\d)+\nCLIENT_NAME: (\w+\s*)+\nMESSAGE: (\w+\s*)+\n\n",msg):
		return True
	else: return False
def parseMessage(msg):
	splitMessage = msg.split('\n')
	#CHAT: [ROOM_REF]
	roomRef= splitMessage[0].split(':')[1].strip()
	#JOIN_ID: [integer identifying client to server]
	joinID= splitMessage[1].split(':')[1].strip()
	#CLIENT_NAME: [string Handle to identifier client user]
	clientName= splitMessage[2].split(':')[1].strip()
	#MESSAGE: [string terminated with '\n\n']
	message=splitMessage[3].split(':')[1].strip()
	return roomRef, joinID, clientName, message
def sendMessage(conn,chatroom, message):
	roomRef, joinID, clientName, message =parseMessage(msg)
	#need to be able to get room ref from chatroomname chatrooom.getref(name)??
	messageMsg= "CHAT: " + roomID
	+ "\nCLIENT_NAME: " + clientName
	+ "\nMESSAGE: " + message
	conn.sendall(message.encode()) #maybe a diffrent conn becasue we are broadcasting to all conns??
	