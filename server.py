import socket
import random
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = sys.argv[1]

n_port = int(port)

#The server will listen to requests
s.bind(('',n_port))
s.listen(5)
print("The server is ready to receive.")

while True:
	c, addr = s.accept()
	address = addr[0]
	print ('Connected with ',address)
	command = c.recv(1024).decode()
# The command is analysed and identified as cmd. 
# cmd can be either EXIT, GET, or an invalid one
	commands = command.split()
	cmd = commands[0]
	c.send('OK'.encode())

	# r_port is received from client
	r_port_str = c.recv(1024)
	r_port = int(r_port_str)

# If the client types 'EXIT' then the connection will terminate.
	if cmd == 'EXIT':
		c.send('The connection ended'.encode())
		break
# If the client types 'GET <filename>' Then the server will send the file
	elif cmd == 'GET':
		# Set up a new tcp connection for file tranferring
		new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		new_s.connect((address, r_port))

		# File transfer
		filename = commands[1]
		file = open(filename, 'rb')
		line = file.read(1024)
		while (line):
			new_s.send(line)
			line = file.read(1024)
		file.close()
		new_s.close()

# If the client types 'PUT <filename>' then the server will save the file
	elif cmd == 'PUT':
		# Set up a new tcp connection for file transferring
		new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		new_s.bind(('',r_port))
		new_s.listen(5)
		new_c, new_addr = new_s.accept()

		# File Transfer
		filename  = commands[1]
		with open('uploaded_'+filename, 'wb') as f:
			data = new_c.recv(1024)
			while (data):
				f.write(data)
				data = new_c.recv(1024)
			f.close()
		new_s.close()

# If the input is neither then it is invalid
	else:
		new_s.send("Invalid request, please try again".encode())


