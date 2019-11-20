# Network-Programming---server-client-file-transfert
Network programming assignment of CS3201

There is several notification before runing the client.py program.
  1) Please use the old version of FileServer.exe
  2) Since there is some decoding issue which will cause the timeout, i've set a timer for ten seconds to break the while loop and close the connection.

Please follow the instruction below:
  1) Enter the IP Address of the server you want to connect to
  2) It will show the destination 'IP Address' : 'Port Number' of the server after connected.
  3) Input the file name with the extension (e.g. test.txt)
  4) It will show the following status
      1. filed open : the test.txt file has already created in your client's file
      2. Send Status: success : which means the server side has sent the file
      3. Open File Status: success : successfully open the file received from the server
      4. Received Data: ...... (the content inside the test.txt)
  5) After coping all the content inside client side, show the status: Receive File test.txt From the Server Successful!
  6) connection closed and exit the code
