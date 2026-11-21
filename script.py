
# All functions defined here

# Define welcome function
def welcome():
    print("Welcome! Are you ready to test your knowledge? You will have 3 categories to choose from, followed by multiple choice questions and your score will be printed at the end.")

# Displays categories for user to choose from
def category():
    print("\nCategories: \n1.) Animals\n2.) Food\n3.) Geography ")
    category_choice = input("Choose your category, enter 1, 2, 3, or 4 to exit: ")
    
    # While loop that matches users input with category and prevents them from entering a key not allowed
    while True:
        print("\nCategories: \n1.) Animals\n2.) Food\n3.) Geography ")
        category_choice = input("Choose your category, enter 1, 2, 3, or 4 to exit: ")
        
        if category_choice == "1":
            print("\nCategory chosen: Animals")
            break
        elif category_choice == "2":
            print("\nCategory chosen: Food")
            break
        elif category_choice == "3":
            print("\nCategory chosen: Geography")
            break
        elif category_choice == "4":
            print("\nThanks for playing, bye!")
            break
        else:
            print("\nPlease enter 1, 2, 3, or 4.")

    






# All functions called here

# Call welcome function
welcome()
category()