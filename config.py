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
TEAL = (0, 128, 128)


tilemap1 = [ 
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', #the Bs represent blocks as in the walls
    'B.........................B....B.......B', #the '.' represent nothing really
    'B.......E.................B..E.B.......B', #the P represents the player
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
tilemap2 = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BB............B..E.E..E................B',
    'B.............B..E.E..E................B',
    'BBBBBBBBBBB...BBBBBBBBBBBBBBB....E..E..B',
    'B...........................B..........B',
    'B..........E................B..........B',
    'B......................................B',
    'B......................................B',
    'B...........................B...E..E...B',
    'B..................P........B..........B',
    'BBBBBBBBBBBBBBBBBBBBB.......BBBBBBBBBBBB',
    'BBBBBBBBBBBBBBBBBBBB.............E.....B',
    'B......E............................E..B',
    'B..E.............................E.....B',
    'B......................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB.........B',
    'B....E...............E.......B.........B',
    'B..........E.................B...E.E...B',
    'B...E..................................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'  ,
]


tilemaps = [tilemap1, tilemap2]
