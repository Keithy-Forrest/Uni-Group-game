import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('Sprites/doux.png').convert_alpha()

BG = (50, 50, 50)

def get_image(sheet, width, height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    return image

frame_0 = get_image(sprite_sheet_image, 24, 24)

run = True
while run: 

    #update background
    screen.fill(BG)

    #display image
    #screen.blit(sprite_sheet_image, (0, 0))

    #show frame image
    screen.blit(frame_0, (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
