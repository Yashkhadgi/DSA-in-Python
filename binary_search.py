def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17]

print("Array:", arr)

target = int(input("Enter a number you want to search: "))

result = binary_search(arr, target)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")