import pygame
from network import Network

width=1500
height=500
#pygame.display - pygame module to control the display window and screen
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
clock = pygame.time.Clock()
clientNumber = 0

class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel =5
    def draw(self,win):
        #draw a rect for Player,  rect(Surface, color, Rect, width=0) -> Rect
        pygame.draw.rect(win,self.color,self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel #coordinates for pygame start at top left
        if self.x > width: self.x = 0
        if self.y > height: self.y = 0
        if self.x < 0: self.x = width
        if self.y <0: self.y = height
        self.update()

    def update(self):
            self.rect = (self.x,self.y,self.width,self.height)


def redrawWindow(win,player, player2):
    win.fill((255,255,255)) #white color
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tuple):
    return str(tuple[0]) + ',' + str(tuple[1])

def main(): #game loop checking for collisons,
                #events and asking server for events
    n = Network()
    print(n.getPos())
    startPos = read_pos(n.getPos())
    run = True
    p = Player(startPos[0],startPos[1],100,100,(0,200,100))
    p2 = Player(0,0,100,100,(0,200,100))
    while run:
        clock.tick(60)
        p2_pos = read_pos(n.send(make_pos( (p.x , p.y) )))
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)


main()
