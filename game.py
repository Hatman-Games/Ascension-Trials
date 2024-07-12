import sys

import pygame
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Ascension Trials | A game by Hatman Games')
        self.screen = pygame.display.set_mode((1080, 720))

        self.clock = pygame.time.Clock()

        self.playerplaceholder = pygame.image.load('data/sprites/player-placeholder.png')
    def run(self):
        while True:
            self.screen.blit(self.playerplaceholder, (500, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)

Game().run()