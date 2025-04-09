def main():
    counts = {}  # Dictionary to store number frequencies

    while True:
        num = input("Enter a number: ")
        if num == "":
            break
        num = int(num)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for number, count in counts.items():
        print(f"{number} appears {count} times.")
if __name__ == '__main__':
    main()
