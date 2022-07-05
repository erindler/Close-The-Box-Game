from json.encoder import ESCAPE
import Func
import os
import pygame

#initialize game and create window
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Close the Box Game")

def main():
    numTiles = Func.start_screen(0, Func.NUMBUTTON, Func.STARTBUTTON, Func.WIN)
    clock = pygame.time.Clock()
    run = True
    tiles, tilerects = Func.create_tile_objs(Func.calc_tile_width(numTiles), Func.TILEHEIGHT, numTiles)
    oneDiceRoll = False
    diceVal = [1, 1]
    turnFinished = True
    turntiles = []
    turnval = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] > 100 and turnFinished:
                diceVal = Func.two_dice_roll(tiles, tilerects)
                turnFinished = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[1] < 100:
                counter = 0
                for rect in tilerects:
                    mouseposition = pygame.mouse.get_pos()
                    if rect.collidepoint(mouseposition[0], mouseposition[1]) == True and tiles[counter].open == True:
                        tiles[counter].close_tile()
                        turntiles.append(tiles[counter])
                    counter += 1
        if Func.check_val(tiles, diceVal) == False:
            for tile in turntiles:
                tile.open == True
                turntiles = []
        Func.draw_window(tiles, tilerects)
        Func.draw_dice(oneDiceRoll, diceVal)
        pygame.display.update()

if __name__ == "__main__":
    main()