def add_three_copies(data_list, data):
    for _ in range(3):
        data_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    copied_list = []
    print("List before:", copied_list)
    add_three_copies(copied_list, message)
    print("List after:", copied_list)
if __name__ == '__main__':
    main()
