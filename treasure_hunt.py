import random


def initialization_grid():
    return [['-'for i in range(5)]for j in range(5)]

def place_treasure():
    return random.randint(0,4),random.randint(0,4)

def give_hint(treasure_row,treasure_col,guess_row,guess_col):
    if guess_row < treasure_row:
        return "move down"
    
    elif guess_row > treasure_row:
        return "move up"
    
    elif guess_col < treasure_col:
        return "move right"
      
    elif guess_col > treasure_col:
        return "move left"
    
    return "TREASURE FOUND"

def treasure_hunt():
    grid = initialization_grid()
    treasure_row,treasure_col = place_treasure()
    print("WELCOME TO THE TREASURE HUNT GAME")
    attempts = 0
    while True:
        print("\nCurrent Grid:")
        for row in grid:
            print(" ".join(row))
        
        #get player guess
        try:
            guess_row = int(input("Enter row number(0-4): "))
            guess_col = int(input("Enter column number(0-4): "))
        except ValueError:
            print("Invalid input,enter valid number(0-4): ")
            continue

        if guess_row not in range(5) or guess_col not in range(5):
            print("Invalid input,enter valid number: ")
            continue

        #if guess cell previously marked
        if grid[guess_row][guess_col] == 'x':
            print("Location already marked,select different location: ")
            continue

        
        #increment attempts counter(adding one to attempts)
        attempts += 1
        
        #checking if guess is correct
        if guess_row == treasure_row and guess_col == treasure_col:
          print(f'TREASURE FOUND IN {attempts}ATTEMPTS')
          break
        else:
            grid[guess_row][guess_col] = 'X'
            hint = give_hint(treasure_col,treasure_row,guess_col,guess_row)
            print(f'Hint:{hint}')


#calling function to run entire game
treasure_hunt()
