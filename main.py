import pygame
from pygame import *

winWidth = 800
winHeight = 600

pygame.init()
screen = pygame.display.set_mode((winWidth, winHeight))
clock = pygame.time.Clock()

white = (255, 255, 255)


def main():
    x = 400
    y = 0
    
    sprite = playerClass(x, y)
    
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            sprite.move_left()
        elif keys[pygame.K_RIGHT]:
            sprite.move_right()
        else:
            sprite.img_index = 0

        sprite.x += sprite.xvel
        sprite.xvel = 0
        
        screen.fill(white)
        screen.blit(sprite.img[sprite.img_index], (sprite.x, sprite.y))
        #screen.blit(pygame.image.load('img/left1.png'), (sprite.x, sprite.y))
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

class playerClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img_index = 0
        self.img = [pygame.image.load('img/left1.png'), pygame.image.load('img/left2.png'), pygame.image.load('img/left3.png'),
                    pygame.image.load('img/left4.png'), pygame.image.load('img/right1.png'),pygame.image.load('img/right2.png'),
                    pygame.image.load('img/right3.png'), pygame.image.load('img/right4.png')]
        self.xvel = 0
        self.yvel = 0
        self.ani_counter = 10
        self.ani_speed = self.ani_counter

    def move_left(self):
        if self.ani_speed != 0:
            self.ani_speed -= 1
        else:
            self.ani_speed = self.ani_counter
            if self.img_index + 1 <= 3:
                self.img_index += 1
            else:
                self.img_index = 0
        self.xvel = -5

    def move_right(self):
        if self.ani_speed != 0:
            self.ani_speed -= 1
        elif self.img_index >= 4:
            self.ani_speed = self.ani_counter
            if self.img_index + 1 <= len(self.img) - 1:
                self.img_index += 1
            else:
                self.img_index = 0
        else:
            if self.img_index < 4:
                self.img_index += 1
        self.xvel = 5
        


main()
