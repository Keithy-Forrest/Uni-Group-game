WIN_WIDTH = 1280
WIN_HEIGHT = 640
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0) #RGB settings so max red(255), 0 green and 0 blue
GREY = (169, 169, 169)
BLACK = (0, 0, 0)
BLUE = (0, 0, 225) #RGB settings so 0 red, 0 green and max blue(225)

tilemap = [ #15 rows because it's 480 pixels and our tiles are 32 bits so 480/32 = 15
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB', #the Bs represent blocks as in the walls
    'B.........................B....B.......B', #the '.' represent nothing really
    'B.......E.................B....B.......B', #the P represents the player
    'B.........................B....B.......B',
    'B.........................B....B.......B',
    'B.....................P................B',
    'B......................................B',
    'B.......BBBBBB.........................B',
    'B...................................B..B',
    'B...................................B..B',
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
