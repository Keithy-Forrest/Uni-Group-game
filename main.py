import pygame 
from sprites import *
from config import *
import sys
import pygame.mixer

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x #storing the attributes
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h)) #this is the red rectangle
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = HealthBar(250, 10, 300, 20, 100) #creating an instance

class Game: #we're starting with our first class
    def __init__(self):
        pygame.init() #initialising pygame
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sprites/bgm.mp3')
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) #setting up the screen as immutable variables so they can't be modified
        self.clock = pygame.time.Clock() #sets up the fps (frames per second)
        self.font = pygame.font.Font('pixeloid.ttf', 32)
        self.running = True
        self.health_bar = health_bar

        self.character_spritesheet = Spritesheet('Sprites/character.png')
        self.enemy_spritesheet = Spritesheet('Sprites/enemy.png')
        self.attack_spritesheet = Spritesheet('Sprites/attack.png')
        self.intro_background = pygame.image.load('Sprites/title.png')

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates() #attack animations and stuff

        self.attack_sound = pygame.mixer.Sound('Sprites/royalty_free_slash.wav')
        self.hit_sound = pygame.mixer.Sound('Sprites/hitHurt_1.wav')
        self.current_tilemap = 0

    def createTilemap(self):
        for i, row in enumerate(tilemaps[self.current_tilemap]):
               for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                   Block(self, j, i)
                if column == "E":
                   Enemy(self, j, i)
                if column == "P":
                  self.player = Player(self, j, i)
                if column == "D":
                   Daughter(self, j, i)
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sprites/bgm.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
                                            

    def new(self):
        self.createTilemap()
        self.remaining_enemies = len(self.enemies)
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
                self.player.attack()
                if self.player.facing == 'up':
                    Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                if self.player.facing == 'down':
                    Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                if self.player.facing == 'left':
                    Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                if self.player.facing == 'right':
                    Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

                    

    def update(self):
        # game loop updates
        self.all_sprites.update()
        remaining_enemies = len(self.enemies)

        if remaining_enemies == 0 and self.current_tilemap <= 2:
            self.transition_screen()  #show transition screen
            self.load_next_tilemap()  #switch to next tilemap
        if remaining_enemies == 0 and self.current_tilemap == 3:
            self.ending_screen()  #displays ending screen
            
    def load_next_tilemap(self):
        if self.current_tilemap < len(tilemaps) - 1:
            self.current_tilemap += 1
            self.new()
        else:
            self.playing = False


    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.health_bar.draw(self.screen)
        
        self.clock.tick(FPS)
        pygame.display.update()


    def main(self):
        #game loop
        while self.playing == True:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def transition_screen(self):
        transition_font = pygame.font.Font('pixeloid.ttf', 32)
        transition_text = transition_font.render("Well done! You defeated all the enemies! Press 'X' to continue.", True, WHITE)
        transition_rect = transition_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
        self.screen.fill(BLACK)
        self.screen.blit(transition_text, transition_rect)
        pygame.display.update()

        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    waiting_for_key = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        waiting_for_key = False

    def game_over_screen(self):
        game_over_font = pygame.font.Font('pixeloid.ttf', 64)
        game_over_text = game_over_font.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 4))
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sprites/game_over.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        restart_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2,
            200,
            50,
            WHITE,
            BLUE,
            "Restart?",
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
                        running = False  #restart the game
                    if quit_button.is_pressed(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        pygame.quit()
                        sys.exit()  #quit the game

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
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sprites/title.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        

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

    def story_screen(self):
        story_text = [
            "You are a brave father adventuring on a quest to save your daughter from the evil goblins.",
            "You must journey through the labyrinth and defeat all the enemies to break the curse.",
            "Use the directional pad to move left, right, up and down.",
            "Use space to eliminate enemies.",
            "Press 'X' to begin your adventure!"
        ]

        story_font = pygame.font.Font('pixeloid.ttf', 24)
        story_text_objects = [story_font.render(line, True, WHITE) for line in story_text]

        story_screen = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        story_screen.fill(BLACK)
    
        y_offset = 200
        for text_surface in story_text_objects:
            text_rect = text_surface.get_rect(center=(WIN_WIDTH / 2, y_offset))
            story_screen.blit(text_surface, text_rect)
            y_offset += 50

        self.screen.blit(story_screen, (0, 0))
        pygame.display.update()

        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    waiting_for_key = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        waiting_for_key = False


    def ending_screen(self):
        # Display the ending message and options
        ending_font = pygame.font.Font('pixeloid.ttf', 32)
        ending_text = ending_font.render("Congratulations! You've defeated all the enemies and rescued your daughter!", True, WHITE)
        ending_rect = ending_text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        restart_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2 + 60,
            200,
            50,
            WHITE,
            BLUE,
            "Restart",
            32
        )   

        quit_button = Button(
            WIN_WIDTH / 2 - 100,
            WIN_HEIGHT / 2 + 120,
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
                        running = False  #restarts the game
                    if quit_button.is_pressed(pygame.mouse.get_pos(), pygame.mouse.get_pressed()):
                        pygame.quit()
                        sys.exit()  #quits the game

            self.screen.fill(BLACK)
            self.screen.blit(ending_text, ending_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            pygame.display.flip()
            self.clock.tick(FPS)


    
g = Game()
g.title_screen()
g.story_screen()  #displays the story screen
g.new()

while g.running:
    g.main()
    if g.current_tilemap < len(tilemaps) - 1:
        g.game_over_screen() #displays game over screen
    else:
        pass
        #g.running = False  #exits the game

pygame.quit()
sys.exit()
