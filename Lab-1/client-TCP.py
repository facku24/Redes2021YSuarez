from socket import *

serverName = '127.0.0.1'
serverPort = 12000

socket_client = socket(AF_INET, SOCK_STREAM)

socket_client.connect((serverName,serverPort))

sentence = input('Input lowercase sentence:')

socket_client.send(sentence.encode())

modifiedSentence = socket_client.recv(1024)

print('From Server: ' + modifiedSentence.decode())

socket_client.close()
