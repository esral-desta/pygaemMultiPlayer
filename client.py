import pygame
from network import Network
import os


pygame.font.init()

BLACK = (0,0,0)

WIDTH = 1000
HEIGHT = 600

WHITE = (255,255,255)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)


HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)

def redrawWindow(win,player, player2):
    win.blit(SPACE,(0,0))
    pygame.draw.rect(win , BLACK, BORDER )
    player.draw(win,WIDTH)
    player2.draw(win,WIDTH)
    draw_results(win,player,player2)
    pygame.display.update()

def draw_results(win,currentplayer,p2):
    currentplayer_health_text = HEALTH_FONT.render(currentplayer.name + str(currentplayer.health),1,WHITE)
    p2_health_text = HEALTH_FONT.render(p2.name + str(p2.health),1,WHITE)

    if currentplayer.name == "esral":
        win.blit(currentplayer_health_text,(10,10))
        win.blit(p2_health_text,(WIDTH-currentplayer_health_text.get_width()-10,10))
    if currentplayer.name == "desta":
        currentplayer_health_text = HEALTH_FONT.render(currentplayer.name + str(p2.op_health),1,WHITE)
        win.blit(p2_health_text,(10,10))
        win.blit(currentplayer_health_text,(WIDTH-p2_health_text.get_width()-10,10))

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        p.hitflag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    print("firing")
                    p.fire()


        p.move(BORDER,WIDTH,HEIGHT)
        # p.fire()
        p.handle_bullets(WIDTH,p2)
        redrawWindow(win, p, p2)

main()