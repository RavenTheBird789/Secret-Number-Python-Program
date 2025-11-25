import random 

def guess():
    random_number = random.randint(1, 10)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and 10: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number: 
            print("Sorry, guess again. Too high.") 

    print(f"Congrats! You have guessed the number {random_number} correctly!")
    
    user_request = input("Would you like to play again? (yes/no): ")
    if user_request == "yes":
        guess();
    elif user_request == "y":
        guess();
    elif user_request == "Yes":
        guess();
    elif user_request == "Y":
        guess();
    else:
        print("Have a nice day!");
        exit();
guess();