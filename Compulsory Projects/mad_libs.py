def mad_libs():
    print("Welcome to the Mad Libs Story!\n")

    name = input("Enter your name: ")
    day = input("Enter a day of the week: ")
    place = input("Enter a place you visited: ")
    person = input("Enter the name of someone you were with: ")
    activity = input("What did you do there? ")
    food = input("What did you eat?? ")

    print("\n--- Your Story ---\n")
    print(f"Last {day}, {name} went to {place} with {person}.")
    print(f"They spent time {activity} and really enjoyed it.")
    print(f"It was an amzaing day, and they eat {food} by the end of it.")
    print("A simple day, but one to remember forever.")

if __name__ == "__main__":
    mad_libs()

    