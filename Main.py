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
    tiles = Func.create_tile_objs(Func.calc_tile_width(numTiles), Func.TILEHEIGHT, numTiles)
    print(Func.calc_tile_width(numTiles))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        Func.draw_window()
        pygame.display.update()

if __name__ == "__main__":
    main()