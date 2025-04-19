import random
def genrt_usrnm(full_nme):
    name_parts = full_nme.split()
    if len(name_parts) < 2:
        return "Please enter full name"
    first_name = name_parts[0].lower()
    last_name = name_parts[-1].lower()

    #basic combo's
    username1 = first_name + last_name
    username2 = first_name[:3] + last_name[-3:]
    username3 = first_name[:4] + last_name[-2:]
    username4 = first_name[-3:] + last_name[:2]

    #add random numbers
    rand_num = random.randint(10,99)
    username5 = first_name + str(rand_num)
    username6 = last_name + str(rand_num)
    username7 = first_name[1:3] + last_name[-4:-1] + str(random.randint(1,9))
    
    usernames = [username1,username2,username3,username4,username5,username6,username7]
    return random.choice(usernames)

while True:
    full_nme = input("Enter your full name or type 'exit' to exit: ")
    if full_nme.lower() == "exit":
        break

    username = genrt_usrnm(full_nme)
    print(username)
    

    print("-" * 50)

