import random

word_list = ["java", "anaconda", "ruby", "python", "html", "javascript", "hermes", "dictionary", "word", "jumble", "treasure", "hunt"]

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

        print("YOUR TASK IS TO GUESS THE ORIGINAL WORD: ")

        print(f'\nCURRENT ROUND:{round_number}')

        print(f'SCRAMBLED WORD IS: {scrambled_word}')

        hint_choice = input("DO YOU WANT A HINT(Y/N): ").lower()
        if hint_choice == "y":
            print(get_hint(word))
        
        guess = input("GUESS ORIGNAL WORD: ").lower()
        while not guess.isalpha():
            print("ENTER VALID WORD: ")
            guess = input("GUESS ORIGNAL WORD: ").lower()

        if guess == word:
                print("GOOD JOB")
                score += 1
        else:
                print("BAD LUCK")
                print(f'CORRECT WORD WAS: {word}')

    print(f'GAME OVER, YOUR FINAL SCORE IS: {score}/{rounds}')

#calling functions
play_game()
