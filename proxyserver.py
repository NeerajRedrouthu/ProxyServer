#!/usr/bin/env python
#_______________________________________________________________________________________________________________________________________________
#												Term Project: ProxyServer 						By Neeraj Redrouthu
#_______________________________________________________________________________________________________________________________________________
																			# required headers.
import socket
import urllib2
import sys
import os
																			# Client program, this is where are the pages are parsed from client to server and server to client.
def client((csocket, caddr)):
	global TCP
	csocket.settimeout(1)														# timeout for the socket 1second
	while True:																# keep looping as long as you have pages to parse...	
		try:
			data = csocket.recv(1024)
			TCP = data.split()
			httpurl = TCP[1]
			url = TCP[4]
			print "URL:",httpurl	
		except :
			break
			
		try:
			if 'GET' in TCP:
				response = urllib2.urlopen(httpurl)								#open the url requested by the client (requesting thr webserver for the page)
				data = response.read()
				csocket.sendall(data)											# send data to client.
				file = open("GET_headers.txt","a")
				for d in TCP[:10]:
					file.write(d)
					file.write(" ")
				file.write("\n")
				file.close()
		except urllib2.URLError:
		 	continue
	csocket.close()															# close the client socket.
	os._exit(0)																# terminate the forked process.	

																			# Here is where it all begins...
default_socket = int(sys.argv[2])													# Server socket as an argument to the program.
hostname = sys.argv[1]														# type in the host name, ex: ranger1||ranger2||ranger3
rc = os.getpid()
clients = 0
client_list = []	

print >>sys.stderr, "Running ProxyServer.py ProcessID:",os.getpid(),"at:",socket.gethostbyname(hostname),":",default_socket
print "_"*30
ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ssocket.bind((socket.gethostbyname(hostname), default_socket))						# Start listening to the binded socket.
ssocket.listen(50)
while True:
	if client_list == []:
		print "Waiting for connection..."										# waiting for a client to connect.
	try:
		(csocket, caddr) = ssocket.accept()									# accept connection from the client.
		clients+=1
		rc=os.fork()															#  fork a child process.
	
		if rc == 0:
			client((csocket, caddr))											# call the child function.
		else:
			csocket.close()
			client_list.append(rc)												# append the forked procedd ID to the list.
			
			if clients == 50:													# finish processing 50 clients if limit reached,( doesn't accept any further requests
				for CID in client_list:
					os.waitpid(CID,0)											# wait for the forked process.
				clients = 0
				client_list = []												# list of forked processes.
																			# Press Ctrl+C to kill the server(Keyboard Interrupt).
	except KeyboardInterrupt:
		print "\nTerminating Server!"
		for CID in client_list:
				try:
					os.waitpid(CID,0)											# wait for any pending forked processes (if any).
				except:
					break
		ssocket.close()														# close the proxyserver's socket.
		sys.exit(0)
