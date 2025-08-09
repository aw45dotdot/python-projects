import random
import turtle

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-"*10)
