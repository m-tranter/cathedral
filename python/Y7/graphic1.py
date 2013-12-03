# graphic1.py - pygame demo

import pygame

# we have to start pygame at the start of the program.
pygame.init()

# set up the graphics window
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
screenRect = screen.get_rect()
pygame.display.set_caption("Click to change colour!")

# define some colours
raspberry = [135,  38,  87]
yellow    = [255, 255,   0]
black     = [  0,   0,   0]
white     = [255, 255, 255]
blue      = [  0,   0, 255]
green     = [  0, 255,   0]
red       = [255,   0,   0]
colours = [raspberry, yellow, black, white, blue, green, red]
cLen = len(colours)
c = done = flag = 0


while not done:
    screen.fill(colours[c])

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    if event.type == pygame.MOUSEBUTTONDOWN and not flag:
        flag = True
        c = (c + 1) % cLen
 
    if event.type == pygame.MOUSEBUTTONUP:
        flag = False
  
    pygame.display.flip()

pygame.quit()
