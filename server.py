import socket
from _thread import *
from player import Player
import pickle

server = "192.168.0.61"
port = 5566

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

# YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
# YELLOW_SPACESHIP = pygame.transform.rotate(
#     pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),
#     90
# )
# RED_SPACESHIP_IMAGE    = pygame.image.load(os.path.join("Assets","spaceship_red.png")) 
# RED_SPACESHIP = pygame.transform.rotate(
#     pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),
#     270
# )

player1 = Player("esral",0,300,50,50,(255,0,0))
player2 = Player("desta",900,300, 50,50, (0,0,255))
players = [player1,player2]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))
            players[0] = data[0]
            players[1] = data[1]

            if not data:
                print("Disconnected")
                break
            else:
                conn.sendall(pickle.dumps(players))
                # if player == 1:

                #     reply = players[0]
                #     conn.sendall(pickle.dumps(reply))
                # if player == 0:
                #     reply = players[1]
                #     conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1