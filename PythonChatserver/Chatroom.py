#Class of type chatroom
#with functions addclient, removeclient


class Chatroom:
	def __init__(self, roomName, roomID):
		self.roomID = roomID
		self.roomName = roomName
		self.clients = {} #list of client objects
			

	def addclient(self, client):
		#if client not in self.clients
		client=self.clients(client.join_ID)
		print("client has been added")
			#else:
				#error
	
	
	def removeclient(self, client):
		#if client in self.clients
		client=self.clients(client.join_ID)
					#removed message
			#else:
					#error
