# myshooter.py  version of Liam Fraser's PyShooter.

import pygame, time
from random import *
pygame.init()

pygame.display.set_caption("My Shooter")
SCREEN = pygame.display.set_mode((400, 300))

pygame.mouse.set_visible(False)
SCREENRECT = SCREEN.get_rect()
SPEED = 40
FPS = pygame.time.Clock()

RASPBERRY = pygame.image.load("pi.png").convert_alpha()
BACK = pygame.image.load("world.jpg").convert()
BOOM = pygame.image.load("boom.png").convert_alpha()
SIGHTS = pygame.image.load("crosshairsmouse.png").convert_alpha()

LASER = pygame.mixer.Sound("laser.wav")
EXPLODE = pygame.mixer.Sound("explode.wav")

class Berry(pygame.sprite.Sprite):
    """The Raspberry."""
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = RASPBERRY
       self.rect = self.image.get_rect()
       self.rect.right = 0
       self.rect.top = self.randY()
       self.raspspeed = 1

    def update(self):
        """Checks to see if raspberry has gone off screen."""
        self.rect.right += self.raspspeed
        if self.rect.left >= SCREENRECT.right:
            self.rect.right = 0
            self.rect.top = self.randY()

    def randY(self):
        "Returns a random y value."""
        temp = SCREENRECT.height - self.rect.height
        return randrange(self.rect.height, temp)
    
class Explosion(pygame.sprite.Sprite):
    """The explosion class."""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = BOOM
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.count = 6

    def update(self):
        """Shows the explosion image for 6 frames."""
        self.count -= 1
        if not self.count:
            self.kill()

class Points:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.value = -1
        self.update()

    def update(self):
        """Score update method."""
        self.value += 1
        msg = "Score: {}".format(self.value)
        self.text = self.font.render(msg, True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.centerx = SCREENRECT.width - self.textRect.width

class Cross(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = SIGHTS
       self.rect = self.image.get_rect()

    def update(self):
        position = pygame.mouse.get_pos()
        self.rect.center = position

rasp = Berry()
score = Points()
crosshairs = Cross()
allsprites = pygame.sprite.Group((rasp, crosshairs))
done = False

while not done:
    SCREEN.blit(BACK, (0,0))
    SCREEN.blit(score.text, score.textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            LASER.play()
            x1 = crosshairs.rect.centerx
            y1 = crosshairs.rect.centery
            hit = rasp.rect.collidepoint(x1, y1)
            if hit:
                score.update()
                rasp.kill()
                bang = Explosion(x1, y1)
                rasp = Berry()
                allsprites.add(rasp, bang)
                EXPLODE.play()

    allsprites.update()
    allsprites.draw(SCREEN)
    FPS.tick(SPEED)
    pygame.display.update()

pygame.quit()
