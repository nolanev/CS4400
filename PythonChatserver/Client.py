


 #class client

class Client:
	def __init__(self, name, conn, addr,join_ID):
		self.name = name
		self.conn = conn
		self.addr = addr
		self.join_ID = join_ID
        
		
	def __str__(self):
		return self.join_ID
		
	def __del__(self):
		print "deleted client"
