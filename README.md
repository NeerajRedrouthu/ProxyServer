# ProxyServer
1. Open terminal and type in make
> this will create an executable version of python script.

2. Then type in ./proxyserver "hostname" ****
>"hostname" is either "ranger1" or "ranger2" or "ranger3" which ever one you are connected to.
> **** is the proxyserver's port number that you want to set.

3.Open up the web browser next and setup the proxy settings accordingly.
IP should be that of "ranger1" ( 161.45.162.70 ) 
IP should be that of "ranger2" ( 161.45.162.71 ) 
IP should be that of "ranger3" ( 161.45.162.51 ) 
and the port number is what you assigned (****).

4. That should be it!! The ProxyServer is good to go ^^

5. oh yah! almost forgot.. press "ctrl+c" (Keyboard Interrupt) 
to terminate the proxyserver.  (the parent process)

NOTE: I'm also Printing the Parent's processID in the first line
just in case, if it doesn't terminate for some reason just type-in 
" kill **** " .(the processID of the parent) to terminate it the hardway.
------------------------------------------------------------------------------------------------------------------------------
Project Description:
In this project we implement a proxyserver to which the client connects in order to access the content 
from a webserver. The proxyserver requests the data for the client and responds to the client by sending 
the response from the webserver to the client.

Program Description:
Line 41: is where the program starts to execute. (lines prior to that are libraries and function definitions).
Lines 41 - 45: consists of the variable declaration/initialization.
Lines 47 -71: is where the proxyserver serves as a server and waits for a client to connect. After the client gets
connected the server, it will fork a child process and call the client function.
Lines 11 - 38: is where the program acts as a client and requests data from the web server and send it to the
client who requested it.
and finally lines 73-81: is where the code catches keyboard interrupt (ctrl+c) exception and 
terminates the program.
------------------------------------------------------------------------------------------------------------------------------
-Neeraj Redrouthu
