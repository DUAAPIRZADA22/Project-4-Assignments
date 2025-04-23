import random
import string

def generate_random_word(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length)).upper()

def hangman():
    print("\n🎉 Welcome to Hangman Game!\n")

    word = generate_random_word()
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6

    while word_letters and lives > 0:
        print(f"Lives left: {lives}")
        print("Used letters:", ' '.join(sorted(used_letters)))
        current_display = [letter if letter in used_letters else '_' for letter in word]
        print("Word: ", ' '.join(current_display))

        guess = input("Guess a letter: ").upper()

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("✅ Good guess!\n")
            else:
                lives -= 1
                print("❌ Wrong guess!\n")
        elif guess in used_letters:
            print("⚠️ You already guessed that letter.\n")
        else:
            print("⚠️ Invalid input. Please enter a letter.\n")

    if lives == 0:
        print(f"\n💀 You lost! The word was: {word}")
    else:
        print(f"\n🎉 You guessed the word: {word}")

hangman()
