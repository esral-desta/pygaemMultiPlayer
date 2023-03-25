import pygame
import os

pygame.font.init()

HEALTH_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)

RED = (255,0,0)
WHITE = (255,255,255)
SPACESHIP_WIDTH  = 50
SPACESHIP_HEIGHT = 50 

MAX_NUM_BULLETS = 3
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),
    90
)

RED_SPACESHIP_IMAGE    = pygame.image.load(os.path.join("Assets","spaceship_red.png")) 
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),
    270
)



class Player():
    def __init__(self,name, x, y, width, height, color):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.health = 10
        # self.health2 = 10
        self.bullet_vel = 3
        self.bullets = []
        self.box = pygame.Rect(self.x,self.y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
        self.hitflag1 = False  # weqie
        self.hitflag2 = False  # teweqie

    def draw(self, win,WIDTH):

        if self.color == (255,0,0):
            # red_health_text = HEALTH_FONT.render("Health :" + str(self.health),1,WHITE)
            # yellow_health_text = HEALTH_FONT.render("Health :" + str(self.health2),1,WHITE)

            # win.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
            # win.blit(yellow_health_text,(10,10))
            # pygame.draw.rect(win,RED,self.box)

            win.blit(YELLOW_SPACESHIP,(self.x,self.y))
            for bullet in self.bullets:
                pygame.draw.rect(win,RED,bullet)
        if self.color == (0,0,255):
            # red_health_text = HEALTH_FONT.render("Health :" + str(self.health),1,WHITE)
            # yellow_health_text = HEALTH_FONT.render("Health :" + str(self.health2),1,WHITE)
    
            # win.blit(red_health_text,(WIDTH-red_health_text.get_width()-10,10))
            # win.blit(yellow_health_text,(10,10))
            # pygame.draw.rect(win,RED,self.box)
    
            win.blit(RED_SPACESHIP,(self.x,self.y))
            for bullet in self.bullets:
                pygame.draw.rect(win,RED,bullet)
        # pygame.draw.rect(win, self.color, self.rect)

    def fire(self):
        if len(self.bullets) < MAX_NUM_BULLETS :
            bullet = pygame.Rect(self.x + self.width,self.y + self.height//2 ,10,5 )
            self.bullets.append(bullet)

    def handle_bullets(self,WIDTH,p2):
        if self.name == "esral":
            for bullet in self.bullets:

                bullet.x += self.bullet_vel 

                if p2.box.colliderect(bullet):
                    print("collition accoured")
                    self.hitflag1 = True
                    self.bullets.remove(bullet)
                if bullet.x > WIDTH:
                    self.bullets.remove(bullet)
        if self.name == "desta":
            for bullet in self.bullets:
                if p2.box.colliderect(bullet):
                    print("collition accoured")
                    self.hitflag1 = True
                    self.bullets.remove(bullet)

                bullet.x -= self.bullet_vel 

                if bullet.x < 0:
                    self.bullets.remove(bullet)
    def move(self,BORDER,WIDTH,HEIGHT):
        keys = pygame.key.get_pressed()
        if self.color == (255,0,0):

            if keys[pygame.K_LEFT] and self.x - self.vel > 0:
                self.x -= self.vel

            if keys[pygame.K_RIGHT] and self.x + self.vel + self.width < BORDER.x :
                self.x += self.vel

            if keys[pygame.K_UP] and self.y - self.vel > 0:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT -15:
                self.y += self.vel
        else:
            if keys[pygame.K_LEFT] and self.x - self.vel > BORDER.x + BORDER.width:
                self.x -= self.vel

            if keys[pygame.K_RIGHT] and self.x + self.vel + self.width < WIDTH:
                self.x += self.vel

            if keys[pygame.K_UP] and self.y - self.vel > 0:
                self.y -= self.vel

            if keys[pygame.K_DOWN] and self.y + self.vel + self.height < HEIGHT -15:
                self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.box = pygame.Rect(self.x,self.y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)