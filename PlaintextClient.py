from socket import *

# constants
serverName = 'localhost'
serverPort = 7

clientSocket = socket(AF_INET, SOCK_STREAM) # Stream = tcp, Dgram = udp
clientSocket.connect( (serverName,serverPort))

#reads input from screen/keyboard

print('Hiya :D please input your command. You can choose between:')
print('1. Random')
print('2. Subtract')
print('3. Add')
sentence = input('Please type your command: ')
sentence = sentence + '\r\n'
byteSentence = sentence.encode() # converts characters to bytes
clientSocket.send(byteSentence)

    #awaiting answer
returnSentence = clientSocket.recv(1024).decode()
match returnSentence:
    case "Random recognized\r\n":
        print('Random: Selects a random number in an inclusive interval between two chosen integers')
        sentence = input('Please type your interval, with a space between the two numbers: ')
    case "Add recognized\r\n":
        print('Add: Returns the sum of two integers')
        sentence = input('Please type the two numbers you want to add up, with a space between them: ')
    case "Subtract recognized\r\n":
        print('Subtract: Takes two integers, and subtracts number 2 from number 1')
        sentence = input('Please type a number, followed by a space and then the number you want to subtract from it: ')
    case _:
        print("Didn't recognize that one")
sentence = sentence + '\r\n'
byteSentence = sentence.encode() # converts characters to bytes
clientSocket.send(byteSentence)
#print('Received: ', returnSentence.decode()) # byte to characters
returnSentence = clientSocket.recv(1024).decode()
print(returnSentence)

clientSocket.close()