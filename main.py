import pygame
from sprites import *
from config import *
import sys

class Game: #we're starting with our first class
    def __init__(self):
        pygame.init() #initialising pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #setting up the screen as immutable variables so they can't be modified#
        self.clock = pygame.time.Clock() #sets up the fps (frames per second)
        self.font = pygame.font.Font('pixeloid.ttf', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('Sprites/character.png')
        self.enemy_spritesheet = Spritesheet('Sprites/enemy.png')
        self.attack_spritesheet = Spritesheet('Sprites/attack.png')
        #self.terrain_spritesheet = Spritesheet('Sprites/terrain.png')
        self.intro_background = pygame.image.load('Sprites/title.png')

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
                    self.player = Player(self, j, i)

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
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if self.player.facing == 'up':
                    Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                if self.player.facing == 'down':
                    Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                if self.player.facing == 'left':
                    Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                if self.player.facing == 'right':
                    Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
                    

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

    def game_over_screen(self):
        game_over_font = pygame.font.Font('pixeloid.ttf', 64)
        game_over_text = game_over_font.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 4))

        restart_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2,
            200,
            50,
            WHITE,
            BLUE,
            "Restart",
            32
        )

        quit_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2 + 60,
            200,
            50,
            WHITE,
            BLUE,
            "Quit",
            32
        )

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.is_pressed(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        running = False  # Restart the game
                    if quit_button.is_pressed(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        pygame.quit()
                        sys.exit()  # Quit the game

            self.screen.fill(BLACK)
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            pygame.display.flip()
            self.clock.tick(FPS)


    def title_screen(self):
        title_font = pygame.font.Font('pixeloid.ttf', 60)
        title_text = title_font.render("Lost in The Labyrinth: A Father's Tale", True, WHITE)
        title_rect = title_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 4))

        start_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2,
            200,
            50,
            WHITE,
            BLUE,
            "Start Game",
            32
        )

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.is_pressed(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        running = False

            self.screen.fill(BLACK)
            self.screen.blit(title_text, title_rect)
            self.screen.blit(start_button.image, start_button.rect)
            pygame.display.flip()
            self.clock.tick(FPS)

    
g = Game()
g.title_screen()  #displays the title screen
g.new()
while g.running:
    g.main()
    g.game_over_screen()  #display the game over screen if the player gets hit



pygame.quit() #quit game
sys.exit() #quit python program
