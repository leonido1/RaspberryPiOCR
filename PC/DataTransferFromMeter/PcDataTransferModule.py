import socket

requstMessage="Give me data"
bufferSize=1024
serverIP='192.168.137.114'
port = 8888


def getDataFromMeter():

     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect((serverIP,port))
     s.send(requstMessage.encode())
     data=(s.recv(bufferSize)).decode()

     s.close()

     return data
