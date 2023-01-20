#  Author: Muhammad Mubeen
# Date: 18/01/2022
# Description: This is the client program for the wordle game
 
import socket
import json 
import argparse
import urllib.request


# Get the words from the link
link = 'https://3700.network/projects/project1-words.txt'
with urllib.request.urlopen(link) as f:
    myfile = f.read()
    print(type(myfile.decode('utf-8')))


# Get the command line arguments and parse them
parser = argparse.ArgumentParser(description="take different flags")
parser.add_argument("-s",help="secure",action="store_true")
parser.add_argument("-p", "--port", help="port")
parser.add_argument("host", help="host")
parser.add_argument("username", help="username")
args = parser.parse_args()

port = args.port
secure = args.s


# Create a TCP/IP socket
HOST = args.host  # The server's hostname or IP address
print(HOST)

# The port used by the server
if args.s == True and args.port == None:
    PORT = 27994
elif args.s == True and args.port != None:
    PORT = int(args.port)
elif args.s == False and args.port != None:
    PORT = int(args.port)
else:
    PORT = 27993

print("YOU ARE CURRENTLY USING PORT: ",PORT)
attempt = 0

# Send the hello message and receive the response
start = {"type": "hello", "northeastern_username": args.username}
sent = json.dumps(start)


# Connect to the server and send the data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    s.sendall(bytes(sent+'\n',encoding='utf-8'))
    data = s.recv(1024)
    print('Received after hello', repr(data))

    # Send the guess message and receive the response
    while True:
        word = input("Enter a word: ")
        while len(word) != 5 or word.lower() not in str(myfile):
            word = input("Invalid Word, Enter word again: ")
        message = {"type": "guess", "id": "foo", "word": word}
        sent2 = json.dumps(message)
        s.sendall(bytes(sent2+'\n',encoding='utf-8'))
        data = s.recv(1024)
        print('Received', repr(data))

        # JSON object must not 'bytes' to access the values
        my_json = data.decode('utf8').replace("'", '"')
        data = json.loads(my_json)

        


        # If the response is bye, then break out of the loop
        # and write the flag to the file
        if data['type'] == 'bye':
            flag_file = open("Secret Flag.txt", "w")
            flag_file.write("Secret Flag: " + data['flag'])
            print(data['flag'])
            flag_file.close()
            break

        print(data['guesses'][attempt]['marks'])
        print(list(word))
        attempt += 1


print('Received', repr(data))
print("Sent", sent2)




