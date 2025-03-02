import random

def banking_system():
    balance = 1000  # Initial balance
    print("\nWelcome to AI-Assisted Banking System")
    print(f"Your current balance: ${balance}")
    
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"Withdrawal successful! New balance: ${balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("\nWelcome to AI-Assisted Guessing Game!")
    print("Guess a number between 1 and 10. You have 3 attempts.")
    
    for _ in range(attempts):
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
            elif guess == secret_number:
                print("Congratulations! You guessed the correct number.")
                return
            else:
                print("Wrong guess. Try again!")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    banking_system()
    guessing_game()
