This app consists of 2 files: 
	server.py
	client.py
	testfile.txt
server.py is the server application
client.py is the client application
testfile.txt is a text file that can be used to test the program. 

The server application was built and tested on ubuntu1604-002.student.cs.uwaterloo.ca
The client application was built and tested on ubuntu1604-006.student.cs.uwaterloo.ca

##Instructions
1. Execute server.py on the server host by typing command line on server host:
	'python3 server.py <n_port>'
   where <n_port> is the port number. 

2. The server should display 'This server is ready to receive'

3. Execute client.py on the client host by typing command line on client host:
	'python3 client.py <server_address> <n_port>'
   Where <server_address> should be the address of the server (ubuntu1604-002.student.cs.uwaterloo.ca) and <n_port> should be the port number same as above. 

4. On client host, when prompted, enter a command. 
   A command can be 'GET <filename>', 'PUT <filename>' or 'EXIT', otherwise invalid. 

5.1. If the command is 'GET <filename>':
	The server will respond 'OK'. 
	The client downloads the file and save a copy called 'saved_<filename>'. 
	The client will display a message saying the file is saved.  
	When completed, the client process will end. 

5.2. If the command is 'PUT <filename>':
	The client will upload the file to the server and display a message.
	When completed, the client process will end. 

5.3. If the command is 'EXIT':
	The server will respond a message and the server process will be terminated. 
	When completed, both the client and server process will end. 

5.4. If the command is not valid: 
	An error message will be shown and the client process will end. 
