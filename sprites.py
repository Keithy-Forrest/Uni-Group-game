import pygame
#from pygame.sprite import _Group
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE #32 pixels
        self.y = y * TILESIZE #64 pixels
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0 #temporary variables that store the change in movement
        self.y_change = 0 #same as top

        self.facing = 'down'

        image_to_load = pygame.image.load("img/single.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed() #list of every key pressed on keyboard
        if keys[pygame.K_LEFT]: #takes away from the x coordinate to move left
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]: #adds to the x coordinate to move right
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]: #takes away from the y coordinate to move up (in pygame, the top is 0 and the very bottom is 480)
            self.y_change -= PLAYER_SPEED #so it's the opposite of what you might think
            self.facing = 'up'
        if keys[pygame.K_DOWN]: #adds to the y coordinate to move down
            self.y_change += PLAYER_SPEED
            self.facing = 'down'


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = (self.game.all_sprites, self.game.blocks)  # Use a tuple to assign both groups
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
             
             

        

