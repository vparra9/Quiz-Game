
# All functions defined here

# Define welcome function
def welcome():
    print("Welcome! Are you ready to test your knowledge? You will have 3 categories to choose from, followed by multiple choice questions and your score will be printed at the end.")

# Displays categories for user to choose from
def category():
    # While loop that matches users input with category and prevents them from entering a key not allowed
    while True:
        print("\nCategories: \n1.) Animals\n2.) Food\n3.) Geography ")
        category_choice = input("Choose your category, enter 1, 2, 3, or 4 to exit: ")
        
        if category_choice == "1":
            print("\nCategory chosen: Animals")
            animalCategory()
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

def animalCategory():
    # Create a dictionary with a list inside
    animal_questions = [
        {
            "question": "What is the fastest land animal?",
            "A": "Lion",
            "B": "Tiger",
            "C": "Cheetah",
            "D": "Horse",
            "answer": "C"
        },
        {
            "question": "How many legs does a spider have?",
            "A": "10",
            "B": "4",
            "C": "12",
            "D": "8",
            "answer": "D"   
        },
        {
            "question": "What is the biggest animal in the world?",
            "A": "Giraffe",
            "B": "Blue whale",
            "C": "Elephant",
            "D": "Great white shark",
            "answer": "A"
        },
        {
            "question": "What animal has the strongest bite force?",
            "A": "Saltwater crocodile",
            "B": "Hippopoptamus",
            "C": "Great white shark",
            "D": "Lion",
            "answer": "A"
        }
    ]

    # for loop to loop through the questions
    # Outer loop goes through each question
    for question in animal_questions:
        print(f"\n{question['question']}")

        # Inner loop goes through each answer choices
        for option in ["A", "B", "C", "D"]:
            print(f"{option}. {question[option]}")

            # Wait for user input
            user_input = input("\nYou answer: ").strip().upper()
    



# All functions called here

# Call welcome function
welcome()
category()