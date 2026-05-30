def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1

input_string = input("Enter nos seperated by space: ")
user_list = [int(x) for x in input_string .split()]
target = int(input("Enter trget element to search: "))
result = linear_search(user_list,target)

if result != -1:
    print("element found at index ", result)
else:
    print("element not found")
    