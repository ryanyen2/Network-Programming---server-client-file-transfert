import socket  # Import socket module
import time

s = socket.socket()  # Create a socket object
port = 12345  # Reserve a port for your service.
timeout = time.time() + 10

host = input('Please Input a IP Address: ')
s.connect((host, port))     # set up the connection
print(u'the server %s:%s has connected.' % (host, port))

file_name = input('Input the file name to be requested from the server: ')
s.sendall(file_name.encode())   # request the file from the server side

with open(file_name, 'wb') as f:    # Open a file i client side
    print('file opened')
    while True:
        data = s.recv(1024)     # receive data in bytes form
        if not data:
            f.close()
            print('file close()')
            break
        print('Send Status: Success')
        print('Open File Status: success')
        x = data.decode("utf-8")        # decode the byte data to string
        x.rstrip('\x00')        # get rid of the '\x00' string
        print('Received data: ', x)
        # write data to a file
        f.write(data)       # write the data to file
        if time.time() < timeout:       # set the time to break the loop, prevent the timeout situation
            break

print('Receive File ' + file_name + ' From the Server Successful!')
s.close()       # close the connection
print('connection closed')
