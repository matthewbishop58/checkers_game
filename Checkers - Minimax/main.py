from pickle import FALSE
from stat import FILE_ATTRIBUTE_COMPRESSED
import pygame
from checkers.constants import SQUARE_SIZE, WIDTH, HEIGHT, RED, WHITE
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)



        if game.winner() != None:
            print(game.winner())
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = FALSE

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)
                

        game.update()

    pygame.quit()

main()