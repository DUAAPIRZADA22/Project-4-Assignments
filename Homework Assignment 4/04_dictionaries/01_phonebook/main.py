def main():
    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input(f"Enter a phone number for {name}: ")
        phonebook[name] = number

    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

if __name__ == '__main__':
    main()
