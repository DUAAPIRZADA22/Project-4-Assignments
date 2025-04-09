import random

def main():
    # Generate a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    guess = -1  # Initialize guess to a number outside the range
    print("I am thinking of a number between 0 and 99...")

    # Loop until the correct guess is made
    while guess != number_to_guess:
        # Ask the user for a guess
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > number_to_guess:
            print("Your guess is too high.")
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
           print(f"Congrats! The number was: {number_to_guess}")
if __name__ == '__main__':
    main()
