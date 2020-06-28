from time import sleep

from entities import Board
from entities import BoardPrinter

from initial_status import initial_status


print('Welcome to the life game')
print('------------------------')
print('')
print('Recreating the initial conditions')
print('')
print('')
board = Board(initial_status)
board_printer = BoardPrinter()

print('Done! Starting the game')

for iteration in range(1, 10):
    print(f'generation: {iteration}')
    print('')
    print('-----------')
    print('')
    board_printer.print_board(board)
    board.next_generation()
    sleep(1)


print('Game Over')