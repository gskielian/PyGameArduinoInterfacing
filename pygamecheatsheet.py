# Pygame Cheat Sheet
# This program should show you the basics of using the Pygame library.
# by Al Sweigart http://inventwithpython.com

# Download files from:
#     http://inventwithpython.com/cat.png
#     http://inventwithpython.com/bounce.wav

import pygame, sys, serial
from pygame.locals import *


ser = serial.Serial('/dev/tty.usbmodem1421',115200)

pygame.init()
fpsClock = pygame.time.Clock()


windowSurfaceObj = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Pygame Cheat Sheet')

catSurfaceObj = pygame.image.load('cat.png')
redColor = pygame.Color(255, 0, 0)
greenColor = pygame.Color(0, 255, 0)
blueColor = pygame.Color(0, 0, 255)
whiteColor = pygame.Color(255, 255, 255)
mousex, mousey = 0, 0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello world!'

soundObj = pygame.mixer.Sound('bounce.wav')

while True:
    windowSurfaceObj.fill(whiteColor)












    windowSurfaceObj.blit(catSurfaceObj, (mousex, mousey))

    msgSurfaceObj = fontObj.render(msg, False, blueColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.topleft = (10, 20)
    windowSurfaceObj.blit(msgSurfaceObj, msgRectobj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            soundObj.play()
            if event.button in (1, 2, 3):
                msg = 'left, middle, or right mouse click'
            elif event.button in (4, 5):
                msg = 'mouse scrolled up or down'

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                msg = 'Arrow key pressed.'
                ser.write('1')
            if event.key == K_RIGHT:
                msg = 'Arrow key pressed.'
                ser.write('2')
            if event.key == K_UP:
                msg = 'Arrow key pressed.'
                ser.write('3')
            if event.key == K_DOWN:
                msg = 'Arrow key pressed.'
                ser.write('4')
            if event.key == K_a:
                msg = '"A" key pressed'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    pygame.display.update()
    fpsClock.tick(500) # pause to run the loop at 30 frames per second
