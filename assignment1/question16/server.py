import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

####### A SIMPLE ILLUSTRATION OF THE TCP SERVER #######

# The port number on which to listen for incoming connections.
PORT_NUMBER = 1235
KEY = input("Enter 16-byte key: ").encode('utf-8')

# Create a socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate the socket with the port
serverSock.bind(('127.0.0.1', PORT_NUMBER))

# Start listening for iuncoming conncetions (we can have at 
# most 100 concetions waiting to be accepted before the server
# starts rejecting new connections)
serverSock.listen(100)

# Keep accepting conncetions forever
while True:

    print("\nWaiting for clients to connect...")

    # Accept a waiting connection
    cliSock, cliInfo = serverSock.accept()

    print("Client connected from: " + str(cliInfo))

    # Receive the data the client has to send.
    # This will receive at most 1024 bytes
    cliMsg = cliSock.recv(1024)
    print("Received: " + str(cliMsg))

    # Decrypt the message
    cipher = AES.new(KEY, AES.MODE_ECB)
    decryptedMsg = cipher.decrypt(cliMsg)
    print("Decrypted: " + str(decryptedMsg))

    # Unpad msg
    unpaddedMsg = unpad(decryptedMsg, AES.block_size)
    print("Unpadded: " + str(unpaddedMsg))
    
    # Decode msg
    finalMsg = unpaddedMsg.decode('utf-8')

    print("Final decrypted message: " + str(finalMsg))

    # Hang up the client's connection
    cliSock.close()
