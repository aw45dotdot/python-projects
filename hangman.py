import random

def hangman():
    sample_words = ["selection", "folder", "audio", "video", "slide", "control"]
    word_to_guess = random.choice(sample_words)
    guess_word = ["_"]*len(word_to_guess)
    max_attempts = 8
    attempts = 0
    guessed_letters = []
    
    print("WELCOME TO HANGMAN\nGUESS THE WORD ONE LETTER AT A TIME")
    print(f'YOU HAVE {max_attempts} ATTEMPTS TO GUESS THE WORD')
    print("WORD: ", " ".join(guess_word))

    while attempts < max_attempts and "_" in guess_word:
        guess = input("\nGUESS A LETTER: ").lower()
        if (len(guess) != 1)or(not guess.isalpha()):
            print("ENTER A SINGLE VALID LETTER: ")
            continue
        if guess in guessed_letters:
            print("LETTER ALREADY GUESSED")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f'GUESS IS CORRECT,{guess} IS IN THE WORD')

            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    word_to_guess[i] = str(guess)
        else:
            attempts += 1
            print(f'WRONG GUESS, YOU HAVE {max_attempts-attempts} ATTEMPTS LEFT')
        print("WORD: ", " ".join(guess_word))
    
    if  "_" not in guess_word:
        print("CONGRATULATIONS YOU GUESSED THE CORRECT WORD")
        print(f'THE WORD WAS: {word_to_guess}')
    
    else:
        print(f'GAME OVER\n CORRECT WORD WAS: {word_to_guess}')

hangman()
