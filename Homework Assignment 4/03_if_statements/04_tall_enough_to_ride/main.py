MIN_HEIGHT = 50 
def main():
    while True:
        height_input = input("How tall are you? ")

        # Stop if user enters nothing
        if height_input == "":
            break
        # Convert input to integer
        height = int(height_input)
        # Check if the user is tall enough
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")
if __name__ == '__main__':
    main()
