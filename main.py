import pygame


#Const
FPS = 60

#Colors
BG = (144, 201, 120)

pygame.init()

screen = pygame.display.set_mode((800, 640))
clock = pygame.time.Clock()

def draw_bg():
    screen.fill(BG)

running = True

while running:
    clock.tick(FPS)

    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    pygame.display.update()

pygame.quit()