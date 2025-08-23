import random
import turtle

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*10)
        
def check_winner(board,row=0,col=0):
    if row==3:
        return None
    #checking current row
    if board[row][0] == board[row][1] == board[row][2] and board[row][0] != " ":
        return board[row][0]
    #checking current column
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
        return board[0][col]
    return check_winner(board,row+1,col+1)

def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        for cell in row:
            if cell==" ":
                return False
    return True

def play_game():
    board=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(" ")
        board.append(row)
    
    
    current_player = "x"
    while True:
        print_board(board)
        print(f"IT'S {current_player}'S TURN")
        row = int(input("Enter the new(0-2): "))
        col = int(input("Enter the new(0-2): "))
        if board[row][col]==" ":
            board[row][col]=current_player
        
        else:
            print("CELL ALREADY TAKEN")
            continue
        
        winner = check_winner(board) or check_diagonals(board)
        if winner:
            print_board(board)
            print(f'{winner} WIN!')
            break
        #check for draw
        if is_full(board):
            print_board(board)
            print("ITS A DRAW")
            break
        
        current_player = "o" if current_player == "X" else "X"

play_game()
