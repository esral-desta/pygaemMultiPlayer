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
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    if players[1].hitflag1 == True:
                    #     pass
                        # print("checked")
                        # print("reducing for ",players[0].name)
                        players[0].health -= 1
                        players[0].hitflag2 = True
                        players[1].hitflag1 == False
                        # print("value set to ",player[0].health)
                    reply = players[0]
                    conn.sendall(pickle.dumps(reply))
                    players[0].hitflag2 = False
                if player == 0:
                    print("not checked")

                    if players[0].hitflag1 == True:
                        # print("checked")
                        # print("reducing for ",players[1].name)
                        players[1].health -= 1
                        players[0].hitflag2 = True
                        players[0].hitflag1 == False
                        # print("value set to ",player[1].health)
                    reply = players[1]
                    conn.sendall(pickle.dumps(reply))
                    players[0].hitflag2 = False
            # conn.sendall()
            # conn.send(pickle.dumps(reply))
            # player1[1].hitflag2 = False
            # player1[2].hitflag2 = False
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