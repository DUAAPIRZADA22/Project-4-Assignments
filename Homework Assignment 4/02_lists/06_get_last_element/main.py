def get_last_element(lst):
    print(lst[-1])
def main():
    lst = []
    n = int(input("How many elements do you want to enter in the list? "))
    
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)
    get_last_element(lst)
if __name__ == '__main__':
    main()
