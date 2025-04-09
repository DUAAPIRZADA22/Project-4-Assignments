import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop counting

def done():
    # Randomly returns True with a likelihood of DONE_LIKELIHOOD
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    
    for i in range(1, 11):  # Counting from 1 to 10
        if done():  # Check if we should stop early
            print("I'm done.")
            return  # Exit the function and return control to main
        print(i, end=" ")

def main():
    chaotic_counting()
if __name__ == '__main__':
    main()
