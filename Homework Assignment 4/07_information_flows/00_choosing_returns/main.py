ADULT_AGE = 18  # Legally considered adult age in the U.S.

def is_adult(age):
    return age >= ADULT_AGE
def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == '__main__':
    main()
