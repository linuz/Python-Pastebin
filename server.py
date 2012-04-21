import socket, os
HOST = "127.0.0.1"
PORT = 1111
ADDR = (HOST,PORT)
BUFFSIZE = 4096

class ppbServer:
	def __init__ (self):
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.bind(ADDR)
		self.server.listen(1)
	def dataAccept(self):
		while 1:
			clientConnection, clientAddress = self.server.accept()
			while 1:
				data = clientConnection.recv(BUFFSIZE)
				if not data: 
					break
				file = self.fileHandle(1, data)
				clientConnection.send("Created file: " + file)
				print "Created file: " + file

	def fileHandle(self, filename, data):
		while os.path.isfile(str(filename) + ".txt"):
			filename += 1		
		file = str(filename) + ".txt"
		fileObject = open(file,"w")
		fileObject.write(data)
		fileObject.close()
		return file



test = ppbServer()
test.dataAccept()
