#From here: https://gist.github.com/daisyzhou/469cb67d5163f274cbd2e8c447a710b3

# N -> Notes for you.
# N -> You failed this one pretty hard buddy. Are you going to learn networking? Probably not.
# N -> If you get bored you could probably have used this -> https://www.geeksforgeeks.org/simple-chat-room-using-python/

# Write a socket-server chat-server that accepts clients that connect to it over TCP. An example client would be netcat or telnet.
#
# The chat server should do 5 things:
#
# Broadcast messages from any client to all other connected clients (like how you would expect a chat room to work).
# Upon connecting prompt the client for their nickname.
#     This nickname is case-sensitive and must be unique on the server.
# If the nickname is already taken the server should tell the user to choose a new nickname.
# Upon entering a valid nickname, the server should:
# send the last 10 lines of chat in the chat room,
# broadcast that the user has connected to the other clients
# send a list of users that are currently connected to the just-connected client.
# Upon disconnecting, the server should:
# broadcast that the user has disconnected.
# If the user is "@mentioned", meaning the message contains @theirnickname, a BEL ('\a') character should be sent to the client that is connected with that nickname.
# Example Interaction:
#
# < Welcome to my chat server! What is your nickname?
# > Jake
# < You are connected with 3 other users: [kelly, alex, jim]
# < [12:04:05] <kelly> yo
# < [12:04:06] <kelly> whats up?
# < [12:04:07] <alex> nothing much!
# < [12:04:09] *Jake has joined the chat*
# > Hey whats going on guys?
# < [12:06:09] <kelly> Nothing much!!

# import socket programming library
import socket

# import thread module
from _thread import *
import threading

nicknames_set = set()
message_hash = []

print_lock = threading.Lock()

# thread function
def threaded(c):

    while True:

        # Ask the user for a nickname, force it to be unique.
        while True:
            print("I make it into the nickname loop")
            c.sendall(bytes("Please enter a Nickname, it must be unique.", 'utf-8'))
            nickname = str(c.recv(1600))

            # You've found a nickname, check to see if it's unique.
            if nickname in nicknames_set:
                c.sendall(bytes("This nickname is already taken. Please choose another.", 'utf-8'))
                continue
            nicknames_set.add(nickname)
            c.sendall(bytes("Thank you for choosing a nickname! Please type to chat.", 'utf-8'))
            break

        continue

        # lock released on exit
        print_lock.release()
        break
    c.close()


def Main():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()
