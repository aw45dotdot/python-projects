dict = {}

while True:
    print("----------Mini Dictionary App----------\n")
    print("1.Add/update an item \n2.Retrieve an item definetion \n3.View all words \n4.Delete an item \n5.Exit app")
    choice = input("\nChoose an option 1-5: ")
    if choice == "1":
        word = input("Enter word to add: ").strip()
        value = input("Enter defenition of word: ").strip()
        dict[word] = value
        print(f'The word {word} successfuly added')

    elif choice == "2":
        word = input("Enter word to see definetion")
        if word in dict:
            print(f'{word}:{value}')
        else:
            print(f'{word} does not exist in dictionary')
