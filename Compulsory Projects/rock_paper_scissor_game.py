import random

def who_wins(user, comp):
    if user == comp:
        return "\n\033[93mIt's a Tie!\033[0m"
    
    if (user == "r" and comp == "s") or (user== "p" and comp== "r") or (user== "s" and comp== "p"):
        return "\n\033[92mYou Win!\033[0m"

    return "\n\033[91mYou Lose!\033[0m"

def main():
    print("\nWelcome to Rock, Paper, Scissors Game!\n")

    print("\033[01m\033[03mChoose 'q' for Quit.\033[0m")
    
    while True:
        user = input("\n\033[01m\033[03mEnter your choice 'r' for rock, 'p' for paper, or 's' for scissors: \033[0m").lower()
        
        if user == "q":
            print("\n\033[94m\033[01m\033[03mThanks for Playing!\033[0m\n")
            break

        if user != "r" and user != "p" and user != "s":
            print("\033[93mPlease Enter a Valid Choice!\033[0m")
            continue
        
        comp = random.choice(["r", "p", "s"])
        print(f"\nComputer's Choice: {comp}")
        
        print(who_wins(user, comp))

if __name__ == '__main__':
    main()
        