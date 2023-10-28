WIN_WIDTH = 1280
WIN_HEIGHT = 640
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 4
ENEMY_SPEED = 2

RED = (255, 0, 0) #RGB settings so max red(255), 0 green and 0 blue
GREY = (169, 169, 169)
BLACK = (0, 0, 0)
BLUE = (0, 0, 225) #RGB settings so 0 red, 0 green and max blue(225)
WHITE = (255, 255, 255)

tilemaps = [ 
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', #the Bs represent blocks as in the walls
    'B.........................B....B.......B', #the '.' represent nothing really
    'B.......E.................B....B.......B', #the P represents the player
    'B.........................B....B.......B', #the Es represent the enemy
    'B.........................B....B.......B',
    'B......................................B',
    'B......................................B',
    'B.......BBBBBB.........................B',
    'B...................................B..B',
    'B...................P...............B..B',
    'B.........................E.........B..B',
    'B...................................B..B',
    'B................BBBBB..............B..B',
    'B....................B.................B',
    'B....................B.................B',
    'B...........E........B.................B',
    'B......................................B',
    'B......................................B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    
]
['BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
 'B.P...........B..E.E..E................B',
 'B.............B..E.E..E................B',
 'BBBBBBBBBBB...BBBBBBBBBBBBBBB....E..E..B',
 'B...........................B..........B',
 'B..........E................B..........B',
 'B......................................B',
 'B......................................B',
 'B...........................B...E..E...B',
 'B...........................B..........B',
 'BBBBBBBBBBBBBBBBBBBBB.......BBBBBBBBBBBB',
 'BBBBBBBBBBBBBBBBBBBB.............E.....B',
 'B......E............................E..B',
 'B..E.............................E.....B',
 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
 ]


class LevelManager:
    def __init__(self, game):
        self.game = game
        self.current_level = 0

    def load_level(self):
        self.game.tilemap = tilemaps[self.current_level]
        self.game.createTilemap()

    def switch_level(self):
        self.current_level += 1
        if self.current_level < len(tilemaps):
            self.load_level()
        else:
            self.game.playing = False
            self.game.victory_screen()

    def check_level_completion(self):
        if len(self.game.enemies) == 0:
            self.switch_level()

            



    
