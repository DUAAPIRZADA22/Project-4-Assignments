import random

def computer_guesses():
    print("🤖 Computer will try to guess the number you're thinking of!")
    print("Think of a number between 1 and 100. Don't tell me!\n")

    low = 1
    high = 100
    tries = 0

    while True:
        if low > high:
            print("Hmm... Seems like something went wrong! 🤔")
            break

        guess = random.randint(low, high)
        tries += 1
        print(f"Is it {guess}?")

        feedback = input("Enter (h) for too high, (l) for too low, (c) for correct: ").lower()

        if feedback == 'c':
            print(f"\n🎉 Yay! The computer guessed your number in {tries} tries.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input, please enter h, l, or c.")

if __name__ == "__main__":
    computer_guesses()


    