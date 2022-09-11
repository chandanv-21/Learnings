from pickle import TRUE
import random
from tkinter import font #for generating random numbers
import pygame
import sys
from pygame.locals import *


#Global variables for game
pygame.font.init()
FPS = 32 #display frequency
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER = 'Gallary/Sprites/Bird.png'
BACKGROUND = 'Gallary/Sprites/Background.png'
PIPE = 'Gallary/Sprites/pipe.png'
score_vlaue = 0
my_font= pygame.font.Font('freesansbold.ttf', 20)
text_surface= my_font.render("HIGH SCORE : ", True, (255,255,0))
# scoreMessage= "HIGH SCORE : "



def welcomeScreen():
    """Shows Welcome images on the Screen."""
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT * .13)  
    basex = 0
    scorex= int(140)
    scorey= int(10)
    scoremx=int(10)
    scoremy=int(30)
    while True:
        for event  in pygame.event.get():
            # If user clicks on cross button close the the game.
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses Space key or UP key then start the game.
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['numbers'][score_vlaue],(scorex,scorey))
                SCREEN.blit(text_surface,(scoremx,scoremy))
                
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT/2)
    basex = 0
    #Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    #my list of upper pipes
    upperPipes =   [ 
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y'] },
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y'] },
        ]

    #my list of lower pipes
    lowerPipes =   [ 
        {'x': SCREENWIDTH+200, 'y': newPipe1[1]['y'] },
        {'x': SCREENWIDTH+200+SCREENWIDTH/2, 'y': newPipe2[1]['y'] },
        ]


    pipeVelx = -4
    playerVely = -9
    playerMaxv = 10 
    playerMinv = -8
    playerAccy = 1

    playerflapAccV = -8 #Player velocity while flapping
    playerFlapped = False #It is true only when bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                welcomeScreen()#$$$$$$$$$$$$$$$$
                # sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key== K_UP):
                if playery > 0:
                    playerVely  = playerflapAccV
                    playerFlapped = True
                    GAME_SOUNDS['fly'].play()

        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes,score)
        # This function will return True if the player is crashed.
        if crashTest:
            welcomeScreen()
            print(f"Your score is {score}")
            return

        #Check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidpos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidpos <= playerMidPos < pipeMidpos + 4:
                #Providing a range for score update
                score =score +1
                print(f"Your score is: {score}")
                GAME_SOUNDS['point'].play()

        if playerVely < playerMaxv and not playerFlapped:
            playerVely += playerAccy

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVely, GROUNDY - playery - playerHeight)

        # Move Pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelx
            lowerPipe['x'] += pipeVelx

        #Add a new pipe when the first pipe is about to go to the left.
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it.
        if upperPipes[0]['x'] < - GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)  
            lowerPipes.pop(0)

        # lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperpipe, lowerpipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperpipe['x'], upperpipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerpipe['x'], lowerpipe['y']))
        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        myDigits = [int(x) for x in list(str(score))]
        width=0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        xoffset = (SCREENWIDTH-width)/2
        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (xoffset, SCREENHEIGHT*.12))
            xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


               
def isCollide (playerx , playery , upperPipes, lowerPipes,score):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['die'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()-15):
            GAME_SOUNDS['die'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and (abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()-15):
            GAME_SOUNDS['die'].play()
            return True

    return False

def getRandomPipe():
    """Generte position of tworandom pipes(one bottom straight and one top rotated."""
    pipeHeight = GAME_SPRITES['pipe'][1].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipex = SCREENWIDTH+10
    y1 = pipeHeight - y2 + offset
    pipe = [ {'x':pipex, 'y':-y1}, #upper pipe
        {'x':pipex, 'y':y2} #lower pipe
    ]
        
    return pipe

    

if __name__ == "__main__":
    #THis will be main point where our game will start.
    pygame.init() #initrialize all pygame modules
    
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by CHANDAN')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Gallary/Sprites/0.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/1.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/2.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/3.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/4.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/5.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/6.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/7.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/8.png').convert_alpha(),
        pygame.image.load('Gallary/Sprites/9.png').convert_alpha())
    
    GAME_SPRITES['message'] = pygame.image.load('Gallary/Sprites/Message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('Gallary/Sprites/Base.png').convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180), 
    pygame.image.load(PIPE).convert_alpha()
    )
    #Game Sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Gallary/Music/die.wav')
    GAME_SOUNDS['fly'] = pygame.mixer.Sound('Gallary/Music/fly.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Gallary/Music/point.wav')


    while True:
        welcomeScreen() #Shows welcome screen to the user untill he presses any button.
        mainGame() # This is the main game function