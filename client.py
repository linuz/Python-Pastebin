
import socket, sys
HOST = "127.0.0.1"
PORT = 1111
ADDR = (HOST,PORT)
BUFFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

input = sys.stdin.read()
if input:
	print input
	client.send(input)
print client.recv(BUFFSIZE)
client.close()
