def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    return first_name, last_name, email

def main():
    first, last, email = get_user_data()
    print("First Name:", first)
    print("Last Name:", last)
    print("Email:", email)

if __name__ == '__main__':
    main()
