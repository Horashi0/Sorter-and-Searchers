import random
data = []

choice = input(
    "\nWhat sort would you like to use? Bubble Sort(1), Insertion Sort(2), Binary Search(3) ")


def generate():
    global data
    data = []
    for i in range(0, 100):
        number = random.randint(0, 100)
        data.append(number)


def bubble_sort(data):
    print("\n------------- Unsorted Data -------------")

    print("\n", data)
    size = len(data)
    for i in range(size):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    print("\n------------- Sorted Data -------------")

    print("\n", data, "\n")


def insert_sort(data):
    print("\n------------- Unsorted Data -------------")
    print("\n", data)
    for i in range(len(data)):
        iicount = 0
        iscount = 0
        global x
        x = data[i]

        j = i - 1
        while x < data[j] and j >= 0:
            data[j+1] = data[j]
            j -= 1
            iicount += 1
            iscount += 1

        data[j+1] = x

    print("\n------------- Sorted Data -------------")

    print("\n", data, "\n")


def binary_search(data, x):

    low = 0
    high = len(data)-1
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if data[mid] < x:
            low = mid + 1
        elif data[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def main(binary_search, data, x):
    x = int(input("What number do you want to find "))
    result = binary_search(data, x)
    if x != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present at data")


def sort():
    global data
    if choice == "1":
        bubble_sort(data)
    if choice == "2":
        insert_sort(data)
    if choice == "3":
        insert_sort(data)
        main(binary_search, data, x)


generate()
sort()
