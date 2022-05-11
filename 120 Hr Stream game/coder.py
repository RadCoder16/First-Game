import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()

#Background Music for the game
mixer.init()
mixer.music.load('Music/bg_music1.mp3')
mixer.music.play()

#Name of the game
name = "RadCoder16"
my_width = 1000
my_height = 500


x = 50
y = 410
vel = 10
width = 50
height = 50

is_jump = False
jumpCount = 10

window = pygame.display.set_mode((my_width, my_height))
pygame.display.set_caption(name)
bg_img = pygame.image.load('images/img3.png')
bg_img = pygame.transform.scale(bg_img,(my_width, my_height))

#Main loop
i = 0
runing = True
while runing:
    
    window.fill((0, 0, 0))
    
    
    window.blit(bg_img,(i,0))
    window.blit(bg_img,(my_width+i,0))
    if(i==-my_width):
        window.blit(bg_img,(my_width+5,0))
        i=0
    i -= 5
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    
    KEYS = pygame.key.get_pressed()
    
    if KEYS[pygame.K_LEFT] and x > vel:
        x -= vel
    
    if KEYS[pygame.K_RIGHT] and x < 1000 - width - vel:
        x += vel
        
    if not(is_jump):    
        if KEYS[pygame.K_UP] and y > vel:
            y -= vel
            
        if KEYS[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
            
        if KEYS[pygame.K_SPACE]:
            is_jump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            is_jump = False
            jumpCount = 10
    
    #This is sort of a character as I will add some sprites as characters to move back and forth
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()