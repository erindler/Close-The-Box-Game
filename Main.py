import Func
import os
import pygame

#Constants
WIDTH = 960
HEIGHT = 540
FPS = 60

#Image
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "pokerCarpet.jpg")), (WIDTH, HEIGHT))


#initialize game and create window
pygame.init()
pygame.mixer.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Close the Box Game")

def draw_window():
    WIN.blit(BACKGROUND, (0, 0))

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()
        pygame.display.update()
        Func.TwodiceRoll()

if __name__ == "__main__":
    main()