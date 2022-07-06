from json.encoder import ESCAPE
import Func
import os
import pygame

#initialize game and create window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Close the Box Game")

def main():
    numTiles = Func.start_screen(0)
    clock = pygame.time.Clock()
    run = True
    tiles, tilerects = Func.create_tile_objs(Func.calc_tile_width(numTiles), Func.TILEHEIGHT, numTiles)
    oneDiceRoll = False
    diceVal = [1, 1]
    turnFinished = True
    diceRolled = False
    turntiles = []
    turnval = 0
    numselected = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] > 100 and turnFinished:
                diceVal = Func.two_dice_roll(tiles, tilerects)
                diceRolled = True
                turnFinished = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] < 100 and diceRolled == True:
                counter = 0
                for rect in tilerects:
                    mouseposition = pygame.mouse.get_pos()
                    if rect.collidepoint(mouseposition[0], mouseposition[1]) == True and tiles[counter].open == True:
                        tiles[counter].open = False
                        turntiles.append(tiles[counter])
                        numselected = True
                    counter += 1
        if Func.check_num(turntiles, diceVal) == True:  #Tests for whether the tiles selected goes over the dice value rolled
            if Func.check_turn(turntiles, diceVal) == True or (len(turntiles) > 0 and Func.check_doubles(diceVal, tiles)): #Tests for whether the tiles selected equals the dice value rolled and Checks for doubles rule
                turnFinished = True
                diceRolled = False
                turntiles = []
                numselected = False
            if len(turntiles) == 1 and len(diceVal) > 1:
                if turntiles[0].tileNum == diceVal[0] and diceVal[0] == diceVal[1]:
                    turnFinished = True
                    diceRolled = False
                    turntiles = []
                    numselected = False
        else:
            for tile in turntiles:
                tile.open_tile()
            turntiles = []
            numselected = False
            turnFinished = False
        if Func.check_val(tiles, diceVal) == False and numselected == False and turnFinished == False: #Tests for whether the game can continue based on dice value rolled
            Func.lose_effect()
            run = False
            main()
        Func.draw_window(tiles, tilerects)
        Func.draw_dice(oneDiceRoll, diceVal)
        pygame.display.update()
        upcounter = 0
        for tile in tiles:
            if tile.open == True:
                upcounter +=1
        if upcounter == 0:
            Func.win_effect()
            run = False
            main()

if __name__ == "__main__":
    main()