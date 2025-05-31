import random

word_list = ["java","anaconda","ruby","python","html","javascript","hermes"]

def jumble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def get_hint(word):
    return f'The first letter of the word is: {word[0].upper()}'

def play_game():
    score = 0
    rounds = 5
    print("WELCOME TO WORD JUMBLE GAME")
    for round_number in range(1, rounds + 1):
        word = random.choice(word_list)
        scrambled_word = jumble_word(word)
