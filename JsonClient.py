from socket import *
import json


# constants
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM) # Stream = tcp, Dgram = udp
clientSocket.connect( (serverName,serverPort))
#reads input from screen/keyboard

print('Hiya :D please input your command. You can choose between:')
print('1. Random')
print('2. Subtract')
print('3. Add')
sentence = input('Please type your command: ')
firstnumber = 0
secondnumber = 0
match sentence:
    case "Random":
        print('Random: Selects a random number in an inclusive interval between two chosen integers')
        firstnumber = int(input('Please type your first number: '))
        secondnumber = int(input('Please type your second number: '))
    case "Add":
        print('Add: Returns the sum of two integers')
        firstnumber = int(input('Please type your first number: '))
        secondnumber = int(input('Please type the number you want to add to it: '))
    case "Subtract":
        print('Subtract: Takes two integers, and subtracts number 2 from number 1')
        firstnumber = int(input('Please type your first number: '))
        secondnumber = int(input('Please type the number you want to subtract from it: '))
    case _:
        print("Not sure that's a real command. I'll send it off and see if the server recognizes it tho")
        firstnumber = "error"
        secondnumber = "error"
x = {
    "Method": sentence,
    "FirstNumber": firstnumber,
    "SecondNumber": secondnumber
}
jpack = json.dumps(x)
jpack = jpack + "\r\n"
byteSentence = jpack.encode() # converts characters to bytes
clientSocket.send(byteSentence)

    #awaiting answer
returnSentence = clientSocket.recv(1024).decode()
returnobj = json.loads(returnSentence)
if(returnobj["ErrorMessage"] != "All good"):
    print("Yeah nah, something went wrong. Here's what I got:")
    print(returnobj["ErrorMessage"])
else:
    print("Method = ", returnobj["Method"])
    print("Result = ", returnobj["Result"])

clientSocket.close()