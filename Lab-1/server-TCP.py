from socket import *

serverName = '127.0.0.1'
serverPort = 12000

# AF_INET establece como protocolo de red a IP
# SOCK_STREAM establece como protocolo de transporte a TCP
def socket_create(addr, port):
    
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind((serverName,serverPort))

    serverSocket.listen(1)

    return serverSocket

# Funcion principal
def main():
    
    severSocket = socket_create(serverName, serverPort)

    print('The server is ready to receive')

    while 1:
        connectionSocket, addr = serverSocket.accept()
    while 1:
        sentence = connectionSocket.recv(1024)
        capitalizedSentence = sentence.decode().upper()
        connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()

if __name__ == "__main__":
        main()
