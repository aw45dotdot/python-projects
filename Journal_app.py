from datetime import datetime

def add_entry():
    entry = input("Write your journal entry: ")
    with open("journal.txt","a")as file:
        date = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
        file.write("[{}] {}\n".format(date,entry))
    print("Entry saved")

def view_entries():
    with open("journal.txt","r")as file:
        print(f'Your journal entries: ')
        index = 0
        for line in file:
            print("{}. {}".format(index,line.strip()))
            index += 1

while True:
    print("\n----------Journal App----------")
    print("\n1.Add entry\n2.View entry\n3.exit")
    choice = input("Choose an option(1-3): ")
    if choice == "1":
        add_entry()
    
    elif choice == "2":
        view_entries()

    elif choice == "3":
        print(f'Exiting journal app')
        break

    else:
        print("Invalid choice")
