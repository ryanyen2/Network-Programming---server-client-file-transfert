import socket  # Import socket module
import time
import sys

port = 12345  # Reserve a port for your service.
# Create a socket object
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Error creating socket: %s" % e)
    sys.exit(1)


# Set up the connection
host = input('PPlease Input a IP Address: ')
try:
    s.connect((host, port))
except socket.gaierror as e:
    print("Address-related error connecting to server: % s" % e)
    sys.exit(1)
except socket.error as e:
    print("Connection error: %s" % e)
    sys.exit(1)
print(u'the server %s:%s has connected.' % (host, port))


file_name = input('Input the file name to be requested from the server: ')
while file_name != 'exit':
    timeout = time.time() + 10

    # request the file from the server side
    try:
        s.sendall(file_name.encode())
    except socket.error as e:
        print("Error sending data: %s" % e)
        sys.exit(1)
    print('Send Status: Success')

    with open(file_name, 'wb') as f:  # Open a file on client side
        print('file opened')
        while True:
            # receive data in bytes form
            try:
                data = s.recv(1024)
            except socket.error as e:
                print("Error receiving data: %s" % e)
                sys.exit(1)

            if not data:
                f.close()
                print('file close()')
                break
            print('Open File Status: success')
            x = data.decode("utf-8")  # decode the byte data to string
            x.rstrip('\x00')
            print('Received data: ', x)

            # write data to a file
            f.write(data)
            if x == 'File':
                print(file_name + " is not found!")     # file not found on server side
                break
            if time.time() < timeout:  # set the time to break the loop, prevent the timeout situation
                print('Receive File ' + file_name + ' From the Server Successful!')
                break
    file_name = input('Input the file name to be requested from the server: ')

s.close()  # close the connection
print('connection closed')
