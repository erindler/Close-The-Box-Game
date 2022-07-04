import Tile
import random
import os
import pygame
import Main

pygame.font.init()

#Constants
WIDTH = 960
HEIGHT = 540
FPS = 60

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
HOTPINK = (255, 0, 127)
DARKBLUE = (0, 0, 139)

#Image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pokerCarpet.jpg")), (WIDTH, HEIGHT))

#Start Screen
tilenums = [9, 10, 11, 12]
BLACKBACKGROUND = pygame.Rect(WIDTH, 10, 50, HEIGHT)
STARTBUTTON = pygame.Rect(WIDTH/2 - 285, HEIGHT/2 - 25, 415, 125)
NUMBUTTON = pygame.Rect(WIDTH/2 + 165, HEIGHT/2 - 25, 125, 125)
STARTSCREENFONT = pygame.font.SysFont("impact", 100)
STARTSCREENTEXT = STARTSCREENFONT.render("CLOSE THE BOX", 1, WHITE)
BUTTONFONT = pygame.font.SysFont("impact", 80)
STARTBUTTONTEXT = BUTTONFONT.render("START", 1, BLACK)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))

numbuttontext = BUTTONFONT.render(str(tilenums[0]), 1, WHITE)
pygame.draw.rect(WIN, BLACK, BLACKBACKGROUND)
pygame.draw.rect(WIN, HOTPINK, STARTBUTTON)
pygame.draw.rect(WIN, DARKBLUE, NUMBUTTON)
WIN.blit(STARTSCREENTEXT, (WIDTH/2 - STARTSCREENTEXT.get_width()/2, 100))
WIN.blit(STARTBUTTONTEXT, (WIDTH/2 - 177.5, HEIGHT/2 - 12.5))
WIN.blit(numbuttontext, (705 - numbuttontext.get_width()/2, HEIGHT/2 - 12.5))
pygame.display.update()

#Start Screen - will provide the number of tiles in the game
def start_screen(numselectionindex, NUMBUTTON, STARTBUTTON, WIN):
    run = True
    while(run):
        numbuttontext = BUTTONFONT.render(str(tilenums[numselectionindex]), 1, WHITE)
        pygame.draw.rect(WIN, DARKBLUE, NUMBUTTON)
        WIN.blit(numbuttontext, (705 - numbuttontext.get_width()/2, HEIGHT/2 - 12.5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseposition = pygame.mouse.get_pos()
                if NUMBUTTON.collidepoint(mouseposition[0], mouseposition[1]) == True:
                    if numselectionindex < 3:
                        numselectionindex += 1
                    else:
                        numselectionindex = 0
                if STARTBUTTON.collidepoint(mouseposition[0], mouseposition[1]) == True:
                    run = False
                    return tilenums[numselectionindex]

#Creates Tile Objects
def create_tile_objs(tileWidth, TILEHEIGHT, numTiles = 9):
    tiles = []
    for i in range(1, numTiles + 1):
        i = Tile.Tile(i, tileWidth, TILEHEIGHT)
        tiles.append(i)
    return tiles

#Calculates the width of the tiles based on the number of tiles in the game
def calc_tile_width(numTiles):
    return WIDTH // numTiles

TILEHEIGHT = 100

#Dice roll stuff
DICESIZE = 75

#Reg Dice
DICE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice1.png")), (DICESIZE, DICESIZE))
DICE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice2.png")), (DICESIZE, DICESIZE))
DICE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice3.png")), (DICESIZE, DICESIZE))
DICE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice4.png")), (DICESIZE, DICESIZE))
DICE5 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice5.png")), (DICESIZE, DICESIZE))
DICE6 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Dice6.png")), (DICESIZE, DICESIZE))

DICE = [DICE1, DICE2, DICE3, DICE4, DICE5, DICE6]

#Rotating Dice
RDICE1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice1.png")), (DICESIZE + 15, DICESIZE + 15))
RDICE2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice2.png")), (DICESIZE + 15, DICESIZE + 15))
RDICE3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice3.png")), (DICESIZE + 15, DICESIZE + 15))
RDICE4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice4.png")), (DICESIZE + 15, DICESIZE + 15))
RDICE5 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice5.png")), (DICESIZE + 15, DICESIZE + 15))
RDICE6 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "RotatingDice6.png")), (DICESIZE + 15, DICESIZE + 15))

RDICE = [RDICE1, RDICE2, RDICE3, RDICE4, RDICE5, RDICE6]

#Displays Dice Roll and Generates Values
def two_dice_roll(tiles):
    dice1Value = random.randint(1, 6)
    dice2Value = random.randint(1, 6)

    for dice in RDICE:
        draw_window(tiles)
        WIN.blit(dice, (WIDTH/2 - DICESIZE - 25, HEIGHT/2 - 5))
        WIN.blit(dice, (WIDTH/2 + 15, HEIGHT/2 - 5))
        pygame.display.update()
        pygame.time.delay(100)

    draw_window(tiles)
    WIN.blit(DICE[dice1Value - 1], (WIDTH/2 - DICESIZE - 20, HEIGHT/2))
    WIN.blit(DICE[dice2Value - 1], (WIDTH/2 + 20, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(1000)
    return [dice1Value, dice2Value]

def one_dice_roll(tiles):
    dice1Value = random.randint(1, 6)

    for dice in RDICE:
        WIN.blit(dice, (WIDTH/2 - DICESIZE/2 - 5, HEIGHT/2 - 5))
        pygame.display.update()
        pygame.time.delay(100)

    draw_window(tiles)
    WIN.blit(DICE[dice1Value - 1], (WIDTH/2 - DICESIZE/2, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(1000)
    return [dice1Value]


#Display Window
def draw_window(tiles):
    WIN.blit(BACKGROUND, (0, 0))
    counter = 0
    for tile in tiles:
        TILE = pygame.transform.scale(pygame.image.load(tile.pic), (tile.tileWidth, tile.tileHeight))
        WIN.blit(TILE, (tile.tileWidth * counter, 0))
        counter += 1

def draw_dice(oneDiceRoll, diceVal):
    if oneDiceRoll == True:
        WIN.blit(DICE[diceVal[0] - 1], (WIDTH/2 - DICESIZE/2, HEIGHT/2))
    else:
        WIN.blit(DICE[diceVal[0] - 1], (WIDTH/2 - DICESIZE - 20, HEIGHT/2))
        WIN.blit(DICE[diceVal[1] - 1], (WIDTH/2 + 20, HEIGHT/2))