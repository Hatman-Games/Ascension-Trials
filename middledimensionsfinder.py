import pygame

class Game:
    ## Initializing the game
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('A game by Hatman Games')
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

        self.playerplaceholder = pygame.image.load('data/sprites/player-placeholder.png')

        self.playerplaceholder_pos = [500, 350]
        self.movement = [False, False, False, False]

def get_middle_dimensions():
    pygame.init()  # Add this line to initialize Pygame
    info = pygame.display.Info()
    width = info.current_w
    height = info.current_h

    middle_width = width // 2
    middle_height = height // 2

    return middle_width, middle_height

# Usage
middle_width, middle_height = get_middle_dimensions()
print(f"Middle dimensions: {middle_width}x{middle_height}")