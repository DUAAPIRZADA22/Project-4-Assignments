MAX_LENGTH = 3
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)
def main():
    lst = []
    n = int(input("How many elements do you want to enter in the list? "))
    
    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)
    shorten(lst)
    print("Final list:", lst)
if __name__ == '__main__':
    main()
