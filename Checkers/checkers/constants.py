from lib2to3.pygram import python_grammar_no_print_statement


import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#rgb colours
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
WOOD = (164, 116, 73)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
