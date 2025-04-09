def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"One day, I dream of owning a magical {word} that changes the world.")
    elif part_of_speech == 1:
        print(f"I dare you to {word} like no one is watching!")
    elif part_of_speech == 2:
        print(f"That sunset was so {word}, it took my breath away.")
    else:
        print("Oops! That's not a valid option.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part)
if __name__ == '__main__':
    main()
