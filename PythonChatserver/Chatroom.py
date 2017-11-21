#Class of type chatroom
#with functions addclient, removeclient


class Chatroom:
	def __init__(self, roomName, roomID):
		self.roomID = roomID
		self.roomName = roomName
		self.clients = {}
		self.mutex = Lock()
	
	def __str__(self):
		return self.join_id
		
#	def addClient(self, clientName, joinID):
#		with self.mutex:
#			if clientName not in self.clients
#				self.clients{joinID}=clientName
#				#added message
			#else:
				#error
	
	
#	def removeClient(self, clientName, joinID):
#		with self.mutex:
#			if clientName in self.clients
#				self.clients{joinID}=NULL
					#removed message
			#else:
					#error
