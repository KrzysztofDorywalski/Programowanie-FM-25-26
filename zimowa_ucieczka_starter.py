import pygame
import random
import sys

#----Ustawienia
WIDTH = 600
HEIGHT = 400
FPS = 60

WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)

#-----init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('zimowa ucieczka')
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)
big_font = pygame.font.SysFont("arial", 40)

#-----pętla główna
while True:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((180, 220, 255))
    pygame.display.flip()