def main():
    # Dictionary of fruit prices
    fruit_prices = {
        'apple': 4.0,
        'durian': 10.0,
        'jackfruit': 3.0,
        'kiwi': 3.0,
        'rambutan': 4.0,
        'mango': 2.0
    }

    total_cost = 0

    # Loop through each fruit and ask for the quantity
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price

    print(f"Your total is ${total_cost:.2f}")
if __name__ == '__main__':
    main()
