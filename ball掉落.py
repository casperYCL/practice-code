import pygame,sys
import random

pygame.init()
class Temp(pygame.sprite.Sprite):
    def __init__(self,filename,initial_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)

        if self.rect.bottom>480:
            self.rect.top=0
            x=random.randint(100,500)

            self.rect.x=x
            

            
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
locationgroup=([50,200],[350,300],[450,200])
Cargroup=pygame.sprite.Group()
for lo in locationgroup:
    speed=[0,random.randint(1,5)]
    # loca=[0,choice([400,500])]
    # loca=random.choice(0,640)
    # loca=250
    Cargroup.add(Temp('images/ball1.png',lo,speed))
    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()###修改
            sys.exit()
            
    pygame.time.delay(20)  
    screen.fill([255,255,255])          
    for carlist in Cargroup.sprites():
        carlist.move()
        screen.blit(carlist.image,carlist.rect)
    pygame.display.update()       











