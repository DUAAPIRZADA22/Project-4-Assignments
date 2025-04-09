def main():
    MAX_VALUE = 10000

    # Initialize the first two Fibonacci numbers
    fib0 = 0
    fib1 = 1

    # Print the first two Fibonacci numbers
    print(fib0, end=" ")
    print(fib1, end=" ")

    while True:
        next_fib = fib0 + fib1
        if next_fib >= MAX_VALUE:
            break
        print(next_fib, end=" ")
        fib0 = fib1
        fib1 = next_fib

if __name__ == '__main__':
    main()
