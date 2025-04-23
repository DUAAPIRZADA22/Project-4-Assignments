import random

def user_guesses():
    print("🎯 Welcome to the Guess the Number Game!")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")

        if not guess.isdigit():
            print("❗ Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    user_guesses()
