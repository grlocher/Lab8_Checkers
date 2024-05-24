import checkers


def game():
    while True:
        squares = int(input('How many squares do you want? Pick a number between 4-16: >> '))
        if 4 <= squares <= 16:
            board1 = checkers.build_board(squares)
            print(board1)
            checkers.get_count(board1)
            checkers.pivot_board(board1)
        else:
            print(f'{squares} is not a valid value, please try again')
            print()


if __name__ == '__main__':
    game()