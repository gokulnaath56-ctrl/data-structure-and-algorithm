# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):

        # Compare each element with pivot
        if array[j] <= pivot:

            # If element smaller than pivot is found
            i += 1

            # Swap element at i with element at j
            array[i], array[j] = array[j], array[i]

    # Swap the pivot element with the greater element
    array[i + 1], array[high] = array[high], array[i + 1]

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quickSort(array, low, high):

    if low < high:

        # Find the pivot element
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


# Main program

data = [2,9,5,12,7,-3]

print("Unsorted Array:")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print("Sorted Array in Ascending Order:")
print(data)
