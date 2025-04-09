def sum_of_numbers(numbers) -> int:
    total: int = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    result = sum_of_numbers(numbers)
    print("The sum of the numbers is:", result)
if __name__ == '__main__':
    main()
