import pygame
width=1500
height=500
#pygame.display - pygame module to control the display window and screen
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel =1
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
        self.rect =(self.x,self.y,self.width,self.height)
def redrawWindow(win,player):
    win.fill((255,255,255)) #white color
    player.draw(win)
    pygame.display.update()

def main(): #game loop checking for collisons,
                #events and asking server for events
    run = True
    p = Player(0,0,100,100,(0,200,100))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p)


main()
