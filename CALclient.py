from socket import *
SN= '192.168.100.4'
SP=12000
CS=socket(AF_INET, SOCK_STREAM) 
CS.connect((SN,SP))
message0=input('enter the operation you want to calculate0 : ').encode()
CS.send(message0)
message=input('enter the operation you want to calculate : ').encode()
CS.send(message)
repfromserv=CS.recv(1024)
print('the reply from the server :',repfromserv)
