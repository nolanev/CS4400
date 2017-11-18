#throw io exception??

def	parseKill(msg):
	#"KILL_SERVICE\n"

def	parseHelo(msg):
	if #"HELO text\n"
		return True
	else return False
def sendHelo(ip, port, conn):
	#"HELO text\nIP:[ip address]\nPort:[port number]\nStudentID:[your student ID]\n"
	String HELOmsg = "HELO test" 
	+ "\n IP: " + ip #this is my ip 
	+ "\n Port: " + port #this is my port num
	+ "\n StudentID: 14335043"
	conn.send(HELOmsg)
	}
	
def	parseJoin(msg):
	#JOIN_CHATROOM: [chatroom name]
	#CLIENT_IP: [IP Address of client if UDP | 0 if TCP]
	#PORT: [port number of client if UDP | 0 if TCP]
	#CLIENT_NAME: [string Handle to identifier client user]
def sendJoin(conn, chatroom, client):
	joinMsg = "JOINED_CHATROOM: " + chatroom.roomName 
	+ "\n SERVER_IP: " [IP address of chat room] #???
	+ "\n PORT: " + [port number of chat room] #???
	+ "\n ROOM_REF: " + chatroom.roomID
	+ "\n JOIN_ID: " + client.joinID
	conn.send(joinMsg)


def	parseError(msg):
	#ERROR_CODE: [integer]
	return errorCode
def sendError(conn, errorcode):
	errorMsg=''
	if errorcode ==1
		errorMsg= "ERROR_DESCRIPTION: "
	conn.send(errorMsg)
	
def	parseExit(msg):
	#LEAVE_CHATROOM: [ROOM_REF]
	#JOIN_ID: [integer previously provided by server on join]
	#CLIENT_NAME: [string Handle to identifier client user]
def sendExit(conn, chatroom, client):
	exitMsg= "#LEFT_CHATROOM: " +chatroom.roomID
	+ "\n JOIN_ID: " client.joinID


def	parseDisconnect(msg):
	#DISCONNECT: [IP address of client if UDP | 0 if TCP]
	#PORT: [port number of client it UDP | 0 id TCP]
	#CLIENT_NAME: [string handle to identify client user]


def	parseMessage(msg):
	#CHAT: [ROOM_REF]
	#JOIN_ID: [integer identifying client to server]
	#CLIENT_NAME: [string identifying client user]
	#MESSAGE: [string terminated with '\n\n']
def sendMessage(conn,chatroom):
	messageMsg= "CHAT: " + chatroom.roomID
	+ "\n CLIENT_NAME: " + client.clientName
	+ "\n MESSAGE: " +[string terminated with '\n\n']
