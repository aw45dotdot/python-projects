sentence = input("Enter any sentence: ")
letters = {"a":0,"e":0,"i":0,"o":0,"u":0}

for y in sentence:
    for z in letters:
        if y == z:
            letters[z] += 1
        
for y in letters:
    print(f'{y,letters[y]}')
    
print("\n")
