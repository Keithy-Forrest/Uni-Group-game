import pygame 
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

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

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        image_to_load = pygame.image.load("Sprites/single.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(BLACK) #makes black transparent
        self.image.blit(image_to_load, (0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

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
            
    def collide_blocks(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x =  hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


        


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
        self.image = pygame.image.load("Sprites/border.png")
        #self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
             
             

        

