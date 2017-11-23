#Class of type chatroom
#with functions addclient, removeclient


class Chatroom:
	def __init__(self, roomName, roomID):
		self.roomID = roomID
		self.roomName = roomName
		self.clients = {} #list of client objects
			

	def addclient(self, client):
		#if client not in self.clients
		self.clients[client.join_ID]=client ##getting stuck at this line
		
	
	def removeclient(self, client):
		#if client in self.clients
		del self.clients[client.join_ID]
