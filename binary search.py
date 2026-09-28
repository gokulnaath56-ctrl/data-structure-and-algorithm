# Iterative Binary Search Function

def binary_search(list1, n):

    low = 0
    high = len(list1) - 1

    while low <= high:

        # Get the middle index
        mid = (high + low) // 2

        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1

        elif list1[mid] > n:
            high = mid - 1

        else:
            return mid  # n is found

    return -1  # Element was not present in the list


# Main program

list1 = [22,29,56,39,49,50,54]
n = int(input("enter your numbers:"))

# Function call
result = binary_search(list1, n)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in list1")
