import enum
import sys      # importing sys to quit the application when needed, via the sys.exit() function
# from random import randrange


# first element is unused so the board is 1-9 instead of 0-8
board_layout = ["unusedElement",
                " ", " ", " ",
                " ", " ", " ",
                " ", " ", " "]

# variable to determine whether or not it's the first run through
first_run = []


class Player(enum.auto):
    PLAYER1 = 'X'
    PLAYER2 = 'O'


def choice_select():
    """Selects choice from main(). 1 prints the board and starts the game for player 1. And 2 exits the game."""
    while True:
        choice = input("1: Start the game\n2: Quit\n")
        if choice in ['1', '2']:
            if choice == '1':
                output_board()
                square_choice(Player.PLAYER1)
                return
            elif choice == '2':
                sys.exit()
        else:
            invalid_input()


def invalid_input():
    """Prints an error upon entering invalid input and asks the user to try again."""
    print("Invalid input. Please try again.")


def update_board(player, player_input):
    """Updates the board layout with the player input, calls the output_board() and check_win() functions
       and finally calls square_choice() with the opposite players number, to make it their turn."""
    if player == Player.PLAYER1:
        board_layout[player_input] = Player.PLAYER1
        output_board()
        if check_win(Player.PLAYER1):
            return True
        if square_choice(Player.PLAYER2):
            return True
    elif player == Player.PLAYER2:
        board_layout[player_input] = Player.PLAYER2
        output_board()
        if check_win(Player.PLAYER2):
            return True
        if square_choice(Player.PLAYER1):
            return True


def output_board():
    """Prints the current state of the board."""
    print(board_layout[1], "|", board_layout[2], "|", board_layout[3])
    print(board_layout[4], "|", board_layout[5], "|", board_layout[6])
    print(board_layout[7], "|", board_layout[8], "|", board_layout[9])


def check_win(player):
    """Checks to see if one of the players has won or if the game is a draw and calls main() if so."""
    bl = board_layout
    if (bl[1] == bl[2] == bl[3] == 'X') or (bl[1] == bl[2] == bl[3] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[4] == bl[5] == bl[6] == 'X') or (bl[4] == bl[5] == bl[6] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[7] == bl[8] == bl[9] == 'X') or (bl[7] == bl[8] == bl[9] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[1] == bl[4] == bl[7] == 'X') or (bl[1] == bl[4] == bl[7] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[2] == bl[5] == bl[8] == 'X') or (bl[2] == bl[5] == bl[8] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[3] == bl[6] == bl[9] == 'X') or (bl[3] == bl[6] == bl[9] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[1] == bl[5] == bl[9] == 'X') or (bl[1] == bl[5] == bl[9] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif (bl[3] == bl[5] == bl[7] == 'X') or (bl[3] == bl[5] == bl[7] == 'O'):
        print(f"Player {player} wins!")
        return True
    elif " " not in bl:
        print("DRAW!")
        return True


def square_choice(player):
    """Asks the user where they want to put X / O. If player parameter 1: print X. if player parameter 2: print O.
       Also checks if the square they selected is already occupied and asks them to select again if it is."""
    while True:
        try:
            player_input = int(input("Select your square: "))
        except ValueError:
            invalid_input()
            continue
        if player_input in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if 'X' in board_layout[player_input] or 'O' in board_layout[player_input]:
                print("Square already occupied. Please try again.")
                continue
        else:
            invalid_input()
            continue
        if update_board(player, player_input):
            return True


def main():
    """
    If it's the first run through of the game, it starts the game regularly by entering the if statement
    and calling choice_select(). If it's the second, or more, it enters the else statement.

    After entering the first_run == 0 if statement, it adds an element to the first_run variable
    to run the else statement in future main() calls (i.e., when the game has finished).

    The else statement resets the board_layout and prints that the game has finished.
    """
    while True:
        for i in range(len(board_layout)):
            board_layout[i] = ' '
            board_layout[0] = 'unusedElement'
        choice_select()


print("This is a Tic Tac Toe game for 2 players!\n"
      "In order to win, you need to have 3 of your symbols in a row,column or diagonal. use 1-9 to input your choice\n"
      "Top row is 1-3, middle row is 4-6, bottom row is 7-9\n")
print("Press 1 to start playing and 2 to quit.\n")

main()
