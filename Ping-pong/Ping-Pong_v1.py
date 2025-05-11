from pygame import *
from random import randint

life = 3
wit_height = 500
wit_witdh = 700
speed = 10
run = True
vin = True
FPS = 60
clock = time.Clock()
#Окно
window = display.set_mode((wit_witdh, wit_height))
display.set_caption('Ping-Pong')
bacgroaud = transform.scale(image.load('fon.jpg'), (wit_witdh, wit_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, image_x , image_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(image_x, image_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def move_player_1(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < wit_height - 80:
            self.rect.y += self.speed
    def move_player_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < wit_height - 80:
            self.rect.y += self.speed




while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
    window.blit(bacgroaud, (0,0))



    display.update()
    clock.tick(FPS)
