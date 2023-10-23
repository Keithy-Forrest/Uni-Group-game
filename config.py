WIN_WIDTH = 640 
WIN_HEIGHT = 480 
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 2
BLOCK_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0) #RGB settings so max red(255), 0 green and 0 blue
BLACK = (0, 0, 0)
BLUE = (0, 0, 225) #RGB settings so 0 red, 0 green and max blue(225)

tilemap = [ #15 rows because it's 480 pixels and our tiles are 32 bits so 480/32 = 15
    'BBBBBBBBBBBBBBBBBBBB', #the Bs represent blocks as in the walls
    'B..................B', #the '.' represent nothing really
    'B..................B', #the P represents the player
    'B...BBB............B',
    'B..................B',
    'B.........P........B',
    'B..................B',
    'B..................B',
    'B......BBB.........B', 
    'B........B.........B',
    'B........B.........B',
    'B..................B',
    'B..................B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]