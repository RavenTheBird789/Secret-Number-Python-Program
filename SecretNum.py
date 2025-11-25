import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number: 
            print("Sorry, guess again. Too high.") 

    print(f"Congrats! You have guessed the number {random_number} correctly!")

guess(10)

user_request = input("Would you like to play again? (yes/no): ")
if user_request == "yes":
    guess(x);
else:
    print("Have a nice day!");
    exit();