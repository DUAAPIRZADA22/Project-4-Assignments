import time

def countdown():
    print("\n\033[1mWelcome to Duaa Pirzada's Countdown Timer!\033[0m")

    while True:
        seconds_input = input("\n\033[1m\033[3mEnter the countdown time in seconds:\033[0m ")
        if seconds_input.isdigit():
            countdown_seconds = int(seconds_input)
            break
        else:
            print("❗ Invalid input. Please enter numbers only.")

    print("\n🕒 Timer is starting...\n")

    while countdown_seconds >= 0:
        minutes, seconds = divmod(countdown_seconds, 60)
        current_time = f"{minutes:02d}:{seconds:02d}"
        print(current_time, end='\r')
        time.sleep(1)
        countdown_seconds -= 1

    print("\n\n\033[1m\033[96m⏰ Time's up! \033[0m\n")

if __name__ == "__main__":
    countdown()
