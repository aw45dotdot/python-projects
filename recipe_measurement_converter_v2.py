import math

#convert cups to grams
def cups_to_grams(cups,ingredient):
    conversion_rate = {"flour": 120,           #1 cup of flour = 120g of flour 
                        "sugar": 200,           #1 cup of sugar = 200g of sugar
                        "butter": 500           #1 cup of butter = 120g of flour
                        }
    if ingredient in conversion_rate:
        grams = cups * conversion_rate[ingredient]
        return grams
    else:
        return "not available"

#convert tbsp to tsp
def tbsp_to_tsp(tbsp):
    return tbsp*3

#convert grams to cup
def grams_to_cups(grams,conversion_rate):
    return grams/conversion_rate

#recipe converter function
def recipe_converter():
    print("\n----------Welcome to recipe converter----------")
    while True:
        print("\n Choose an option: ")
        print("1.Convert cups to grams\n2.Convert Tablespoon to Teaspoon\n3.Convert grams to cups\n4.Exit")
        choice = input("Choose an option 1-4: ")
        if choice == "1":
            cups = float(input("How many cups?: "))
            conversion_rate = float(input("How many grams in a cup for ingredient?: "))
            result = cups_to_grams(cups,ingredient)
            print(f'{result} grams')

        elif choice == "2":
            tbsp = float(input("How many tablespoon?: "))
            result = tbsp_to_tsp(tbsp)
            print(f'{result} tsp')

        elif choice == "3":
            grams = float(input("How many grams?: "))
            conversion_rate = float(input("How many cups in ingredient?: "))
            result = cups_to_grams(grams,conversion_rate)
            print(f'{result} cups')

        elif choice == "4":
            print(f'Exiting recipe measurement app')
            break

        else:
            print(f'Enter valid number/option')

recipe_converter()
