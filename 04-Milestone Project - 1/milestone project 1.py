

def display_board(rows):
    fillrow = "-----------"
    print(rows[0])
    print(fillrow)
    print(rows[1])
    print(fillrow)
    print(rows[2])


def choose_square():
    square = int(input("Choose your square using the numpad to the right as a grid: "))

    if square in [1, 2, 3]:
        row = 2
        if square == 1:
            col = 1
        elif square == 2:
            col = 2
        elif square == 3:
            col = 3
    elif square in [4, 5, 6]:
        row = 1
        if square == 4:
            col = 1
        elif square == 5:
            col = 2
        elif square == 6:
            col = 3
    elif square in [7, 8, 9]:
        row = 0
        if square == 7:
            col = 1   # 1
        elif square == 8:
            col = 2   # 5
        elif square == 9:
            col = 3   # 9

    return row, col


def string_index(col):
    idx = (col*4) - 3
    return idx


def whose_turn(turn):

    print("             ")
    if turn % 2 == 0:
        print("Player 1's turn")
        return 1
    else:
        print("Player 2's turn")
        return 2


def mark_spot(player, row, col):
    markers = {1: "X", 2: "O"}
    str_idx = string_index(col)
    rows[row] = rows[row][:str_idx] + markers[player] + rows[row][str_idx+1:]

    return rows

def result(rows, player):
    interesting_squares = [[rows[i][1], rows[i][5], rows[i][9]] for i in range(3)]

    if check_for_win(interesting_squares):
        print(f"Player {player} won!!!")
        return True
    elif check_for_draw(interesting_squares):
        return True
    else:
        return False


def check_for_win(squares):

    for row in squares:
        if row[0] == row[1] == row[2] == "X" or row[0] == row[1] == row[2] == "O":
            return True

    for i in range(3):
        col = [squares[j][i] for j in range(3)]
        if col[0] == col[1] == col[2] == "X" or col[0] == col[1] == col[2] == "O":
            return True

    diags = [[squares[i][i] for i in range(3)], [squares[i][2-i] for i in range(3)]]
    for diag in diags:
        if diag[0] == diag[1] == diag[2] == "X" or diag[0] == diag[1] == diag[2] == "O":
            return True

    return False


def check_for_draw(squares):
    empty = 0
    for i in range(3):
        for j in range(3):
            if squares[i][j] == " ":
                empty += 1

    if empty > 0:
        #print("Squares remaining, play on")
        return False
    elif empty == 0:
        print("No winner and no squares left. Draw.")
        return True

def setup():
    turn = 0
    rows = ["   |   |   ", "   |   |   ", "   |   |   "]
    play_on = True

    return turn, rows, play_on


player1 = input("Player 1's name: ")
print("I think player 1 is an angel...")

player2 = input("Player 2's name: ")

turn, rows, play_on = setup()

display_board(rows)

while play_on:
    # Keep playing until draw or win

    player = whose_turn(turn)

    row, col = choose_square()

    rows = mark_spot(player, row, col)

    display_board(rows)

    if result(rows, player):
        play_on = False

    turn += 1

    if play_on is False:
        replay = input("Do you want to replay? (Y/N) ")
        if replay == "Y":
            turn, rows, play_on = setup()
            display_board(rows)






