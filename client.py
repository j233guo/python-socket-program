import socket
import random
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = sys.argv[2]
n_port = int(port)
sname = sys.argv[1]

s.connect((sname, n_port))

# The client will send a command
command = input('Please enter a command: ')
s.send(command.encode())
commands = command.split()
cmd = commands[0]
print(s.recv(1024))

# The client creates a random port number and send it to server
r_port = random.randint(1024, 65535)
while r_port == n_port:
	r_port = random.randint(1024, 65535)
r_port_str = str(r_port)
s.send(r_port_str.encode())

# If the command is EXIT then the connection will be terminated.
if cmd == 'EXIT':
	print(s.recv(1024))
	s.close()
# If the command is a valid GET then it will print the file and save the file locally
elif cmd == 'GET':
	#Established new tcp connection
	new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	new_s.bind(('',r_port))
	new_s.listen(5)
	new_c, new_addr = new_s.accept()

	fn = commands[1]
	with open('saved_'+fn, 'wb') as f:
		data = new_c.recv(1024)
		while (data):
	# Write the received data into a local file
			f.write(data)
			data = new_c.recv(1024)
		f.close()
	print('File saved')
	new_s.close()
	s.close()

# If the command is a valid PUT then it will upload the file onto the server
elif cmd == 'PUT':

	# Establish new TCP connection
	new_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	new_s.connect((sname, r_port))

	fn = commands[1]
	file = open(fn, 'rb')
	line = file.read(1024)
	while (line):
		new_s.send(line)
		line = file.read(1024)
	file.close()
	print('File uploaded')
	new_s.close()
	s.close()
# If the command is not valid then it will print a message and stop
else:
	print(s.recv(1024))
	s.close()
