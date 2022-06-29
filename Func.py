import Tile
import random
import os
import pygame
import Main

#Constants
WIDTH = 960
HEIGHT = 540
FPS = 60


#Image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pokerCarpet.jpg")), (WIDTH, HEIGHT))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Start Screen - will provide the number of tiles in the game
def start_screen():
    pass



    #return numTiles

#Display Window
def draw_window():
    WIN.blit(BACKGROUND, (0, 0))

#Creates Tile Objects
def create_tile_objs(numTiles = 9):
    tiles = []
    for i in range(1, numTiles + 1):
        i = Tile.Tile(i)
        tiles.append(i)
    return tiles

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
def two_dice_roll():
    dice1Value = random.randint(1, 6)
    dice2Value = random.randint(1, 6)

    for dice in RDICE:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(dice, (WIDTH/2 - DICESIZE - 25, HEIGHT/2 - 5))
        WIN.blit(dice, (WIDTH/2 + 15, HEIGHT/2 - 5))
        pygame.display.update()
        pygame.time.delay(100)

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(DICE[dice1Value - 1], (WIDTH/2 - DICESIZE - 20, HEIGHT/2))
    WIN.blit(DICE[dice2Value - 1], (WIDTH/2 + 20, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(1000)
    return dice1Value, dice2Value

def one_dice_roll():
    dice1Value = random.randint(1, 6)

    for dice in RDICE:
        WIN.blit(BACKGROUND, (0, 0))
        WIN.blit(dice, (WIDTH/2 - DICESIZE/2 - 5, HEIGHT/2 - 5))
        pygame.display.update()
        pygame.time.delay(100)

    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(DICE[dice1Value - 1], (WIDTH/2 - DICESIZE/2, HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(1000)
    return dice1Value