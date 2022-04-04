from socket import *
s = socket.socket() 
serverName = '192.168.100.4'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

    while(True):
        equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")
        s.send(equ.encode())
        result = s.recv(1024).decode()

        if result == "Quit":
            print("Closing client connection, goodbye")
            break
        elif result == "ZeroDiv":
            print("You can't divide by 0, try again")
        elif result == "MathError":
            print("There is an error with your math, try again")
        elif result == "SyntaxError":
            print("There is a syntax error, please try again")
        elif result == "NameError":
            print("You did not enter an equation, try again")
        else:
            print("The answer is:", result)

    s.close 				 # Close the socket when done

except (IndexError, ValueError):
    print("You did not specify an IP address and port number")
