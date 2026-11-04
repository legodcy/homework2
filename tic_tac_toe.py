board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
         [0, 3, 6], [1, 4, 7], [2, 5, 8],
         [0, 4, 8], [2, 4, 6]]
player = "X"
winner = ""
moves = 0

while winner == "" and moves < 9:
    print()
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

    number = int(input("Player " + player + " (1-9): "))

    if number < 1 or number > 9 or board[number - 1] in ["X", "O"]:
        print("Invalid move, try again")
    else:
        board[number - 1] = player
        moves += 1

        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]]:
                winner = player

        if player == "X":
            player = "O"
        else:
            player = "X"

print()
print(board[0], "|", board[1], "|", board[2])
print(board[3], "|", board[4], "|", board[5])
print(board[6], "|", board[7], "|", board[8])

if winner != "":
    print("Player", winner, "wins!")
else:
    print("Draw!")
