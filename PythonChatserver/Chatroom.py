#Class of type chatroom
#with functions addclient, removeclient


class Chatroom:
	def __init__(self, roomName, roomID):
		self.roomID = roomID
		self.roomName = roomName
		self.clients = {} #list of client objects
			
	def __str__(self):
		return self.join_id
		
	def addclient(self, client):
			if client not in self.clients
				self.clients{client.join_ID}=client
				print(" client has been added")
			#else:
				#error
	
	
	def removeclient(self, clientName, joinID):
			if client in self.clients
				self.clients{joinID}=NULL
					#removed message
			#else:
					#error
