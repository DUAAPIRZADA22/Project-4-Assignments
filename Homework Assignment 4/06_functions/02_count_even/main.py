def count_even(lst):
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when the user presses Enter without input
            break
        try:
            num = int(user_input)  # Convert the input to an integer
            lst.append(num)  # Add the number to the list
        except ValueError:
            print("Please enter a valid integer.")
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"The number of even numbers in the list is: {even_count}")

def main():
    numbers = []  # Empty list to store the numbers
    count_even(numbers)
if __name__ == '__main__':
    main()
