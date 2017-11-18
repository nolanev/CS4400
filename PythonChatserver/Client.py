from socket import *
import sys
import os
import os.path
from thread import *

 #class client

class Client:
    def __init__(self, handle, conn, addr,join_id):
        self.handle = handle
        self.conn = conn
        self.addr = addr
		self.join_id = join_id
        
		
    def __str__(self):
        return self.join_id

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.join_id == other.join_id    #what is this for??

        return False