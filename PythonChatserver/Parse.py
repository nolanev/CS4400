#throw io exception??

##########KILL##########
def	checkKill(msg):	
	if match ("KILL_SERVICE\n",msg)
		return True
	else return False

##########HELO##########
def	checkHelo(msg):
	if match ("HELO text\n",msg)
		return True
	else return False
def sendHelo(ip, port, conn):
	#"HELO text\nIP:[ip address]\nPort:[port number]\nStudentID:[your student ID]\n"
	String HELOmsg = "HELO text" 
	+ "\n IP: " + ip #this is my ip 
	+ "\n Port: " + port #this is my port num
	+ "\n StudentID: 14335043"
	conn.send(HELOmsg)
	}

##########JOIN##########
def	checkJoin(msg):
	if match("JOIN_CHATROOM: (\w+\s*)+\nCLIENT_IP: (\d)\nPORT: (\d)\nCLIENT_NAME: (\w+\s*)+\n",msg)
		return True
	else return False
def parseJoin(msg):
	splitMessage = msg.split('\n')
	#JOIN_CHATROOM: [chatroom name]
    chatroomName = splitMessage[0].split(':')[1].strip()
	#CLIENT_IP: [IP Address of client if UDP | 0 if TCP]
	clientIP =splitMessage[1].split(':')[1].strip()
	#PORT: [port number of client if UDP | 0 if TCP]
	clientPort=splitMessage[2].split(':')[1].strip()
	#CLIENT_NAME: [string Handle to identifier client user]
    clientName = splitMessage[3].split(':')[1].strip()
   	return chatroomName, clientIP, clientPort, clientName
def sendJoin(conn, chatroom, client):
	joinMsg = "JOINED_CHATROOM: " + chatroom.roomName 
	+ "\n SERVER_IP: " [IP address of chat room] #???
	+ "\n PORT: " + [port number of chat room] #???
	+ "\n ROOM_REF: " + chatroom.roomID
	+ "\n JOIN_ID: " + client.joinID
	conn.send(joinMsg)

##########ERROR##########	
def	checkError(msg):
	if !match("ERROR_CODE: (\d) +\n)",msg)
		return 0
	else
		errorcode= msg.split(':')[1].strip()
	return errorCode
def sendError(conn, errorcode):
	errorMsg=''
	if errorcode ==1
		errorMsg= "ERROR_DESCRIPTION: "
	conn.send(errorMsg)

##########EXIT##########		
def	checkExit(msg):
	if match("LEAVE_CHATROOM: (\w+\s*)+\n JOIN_ID: (\d)+\n CLIENT_NAME: (\w+\s*)+\n",msg):
		return True
	else return False	
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
	+ "\n JOIN_ID: " client.joinID
	conn.send(exitMsg)

##########DISCONNECT##########	
def	checkDisconnect(msg):
	if match("DISCONNECT: (\d) +\n PORT: (\d) +\n CLIENT_NAME: (\w+\s*)+\n",msg)
		return True
	else return False
def parseDisconnect(msg):
	splitMessage = msg.split('\n')
	#DISCONNECT: [IP address of client if UDP | 0 if TCP]
	clientIP= splitMessage[0].split(':')[1].strip()
	#PORT: [port number of client it UDP | 0 id TCP]
	clientPort=splitMessage[1].split(':')[1].strip()
	#CLIENT_NAME: [string handle to identify client user]
	clientName=splitMessage[3].split(':')[1].strip()
	
	#really from here i want to be able to rturn my client object as below but i need join id
	client=clients[joinID]
	return client
	


##########BROADCAST##########	
def	checkMessage(msg):
	if match("CHAT: (\d) +\n JOIN_ID: (\d)+\n CLIENT_NAME: (\w+\s*)+\n MESSAGE: (\w+\s*)+\n\n",msg)
		return True
	else return False
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
	+ "\n CLIENT_NAME: " + clientName
	+ "\n MESSAGE: " + message
	conn.send(message) #maybe a diffrent conn becasue we are broadcasting to all conns
	