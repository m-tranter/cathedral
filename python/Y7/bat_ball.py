# bat_ball.py: simple pygame demo

import pygame
pygame.init()

# initialise variables
FPS = 150               # Frames Per Second
size = 300, 300         # size of pygame window
title = "Bat and Ball"  # window title
bat_gap = 50            # gap between bat and bottom of window
xSpeed = ySpeed = 1     # speed of ball
ball_size = 40, 40      # size of ball surface
ball_rad = 20           # radius of ball
bat_size = 64, 12       # size of bat

# define colours
raspberry = [135,  38,  87]
black     = [  0,   0,   0]
white     = [255, 255, 255]
blue      = [  0,   0, 255]
green     = [  0, 255,   0]
red       = [255,   0,   0]
yellow    = [255, 255,   0]

# set up the graphic window 
width, height = size
screen = pygame.display.set_mode(size)
screenrect = screen.get_rect()

# give the window a title
pygame.display.set_caption(title)

# This makes the normal mouse pointer invisible in graphics window
pygame.mouse.set_visible(False)

# make surface for bat
bat_surf = pygame.Surface(bat_size)
bat_surf.fill(raspberry)        
batrect = bat_surf.get_rect()

# make surface for ball
ball_surf = pygame.Surface((ball_size))
ball_surf.set_colorkey(black)
ballrect = ball_surf.get_rect()
center = ballrect.centerx, ballrect.centery
ball = pygame.draw.circle(ball_surf, blue, center, ball_rad)

# puts the bat center of screen, near the bottom
batrect.center = screenrect.centerx, (screenrect.bottom - bat_gap)

# make a text object
font = pygame.font.Font(None, 36)
text = font.render("Game Over.", True, red)
textRect = text.get_rect()
textRect.centerx = screenrect.centerx
textRect.centery = screenrect.centery

# loop until the user clicks the close button
done=False

# create a timer to control how often the screen updates
clock = pygame.time.Clock()

# main game loop
while done==False:
    # fill the screen with a colour
    screen.fill(yellow)

    # event handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 

    # moves bat in accordance with the mouse position
    x, y = pygame.mouse.get_pos()
    batrect.centerx = x

    # move the ball
    ballrect.left += xSpeed
    ballrect.top += ySpeed

    # collision detection
    if ballrect.bottom == batrect.top:
        if ballrect.left <= batrect.right and ballrect.right >= batrect.left:
            ySpeed = -ySpeed

    # check if the ball is going off screen
    if ballrect.left < 0 or ballrect.right > width:
        xSpeed = -xSpeed
    if ballrect.top < 0:
        ySpeed = -ySpeed

    # print "Game Over" if the ball leaves screen
    if ballrect.top > screenrect.bottom:
        screen.blit(text, textRect)

    # blit the images to the screen
    screen.blit(bat_surf, batrect)
    screen.blit(ball_surf, ballrect)

    # set the loop to fps cycles per second
    clock.tick(FPS)

    #  update the display
    pygame.display.flip()

# close pygame
pygame.quit()
