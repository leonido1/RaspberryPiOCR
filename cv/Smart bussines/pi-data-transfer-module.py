import socket
import time
import threading 
from PIMeterReaderModule import*


getDataCommand="Give me data"
PORT=8888
HOST='192.168.137.114'
bufferSize=1024


def main ():
    
   calcThread=threading.Thread(target=sample)
   netWorkThread=threading.Thread(target=serveClients)

   calcThread.start()
   netWorkThread.start()

   calcThread.join()
   netWorkThread.join()




def serveClients():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.bind((HOST,PORT))

    s.listen(10)
    print("------server set ------")

    while True:
        conn,addr=s.accept()
        print("--accepted---")
        
        command=(conn.recv(bufferSize)).decode()
        print(command)
        
        if(command==getDataCommand):
            conn.send(str( Meter.meterRead).encode())
            continue

    s.close()        



if __name__ == 'main':
    main()
