import socket  # Import socket module
import time

s = socket.socket()  # Create a socket object
port = 12345  # Reserve a port for your service.
timeout = time.time() + 10

host = input('PPlease Input a IP Address: ')
s.connect((host, port))
print(u'the server %s:%s has connected.' % (host, port))

file_name = input('Input the file name to be requested from the server: ')
s.sendall(file_name.encode())

with open(file_name, 'wb') as f:
    print('file opened')
    while True:
        data = s.recv(1024)
        if not data:
            f.close()
            print('file close()')
            break
        print('Send Status: Success')
        print('Open File Status: success')
        x = data.decode("utf-8")
        x.rstrip('\x00')
        print('Received data: ', x)
        # write data to a file
        f.write(data)
        if time.time() < timeout:
            break

print('Receive File ' + file_name + ' From the Server Successful!')
s.close()
print('connection closed')
