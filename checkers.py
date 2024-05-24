from numpy import random
from numpy import ndarray
from numpy import transpose

board_squares = ['Empty', 'Black', 'Red']


def build_board(squares: int) -> ndarray:
   return random.choice(board_squares, (squares, squares))


def get_count(board1) -> int:
    empty = board1 == 'Empty'
    black = board1 == 'Black'
    red = board1 == 'Red'
    print()
    print(f'There are {empty.sum()} empty squares.')
    print(f'There are {black.sum()} black squares.')
    print(f'There are {red.sum()} red squares.')
    print()


def pivot_board(board1):
    transpose_board = transpose(board1)
    print('This is the original board.')
    print(board1)
    print()
    print('This is the board transposed.')
    print(transpose_board)
    print()


if __name__ == '__main__':
    print('Running the checkers.py file directly')
    print()