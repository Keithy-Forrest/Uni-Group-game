import pygame
from sprites import *
from config import *
import sys

class Game: #we're starting with our first class
    def __init__(self):
        pygame.init() #initialising pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #setting up the screen as immutable variables so they can't be modified#
        self.clock = pygame.time.Clock() #sets up the fps (frames per second)
        #self.font = pygame.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('Sprites/character.png')
        self.enemy_spritesheet = Spritesheet('Sprites/enemy.png')
        #self.terrain_spritesheet = Spritesheet('Sprites/terrain.png')

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates() #attack animations and stuff

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B": #detects for a B in the tilemap and places a tile representing a block in its local
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P": #detects for a P in the tilemap and places the player
                    Player(self, j, i)

    def new(self):
        self.createTilemap()
        #a new game starts
        self.playing = True #useful for checking when a player dies or not

        self.all_sprites = pygame.sprite.LayeredUpdates() #contains all of our sprites
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates() #attack animations and stuff

        self.createTilemap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #game loop updates
        self.all_sprites.update()


    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing == True:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

#self.character_spritesheet = Spritesheet('Sprites/character.png')
#self.terrain_spritesheet = Spritesheet('Sprites/terrain.png')

pygame.quit() #quit game
sys.exit() #quit python program
