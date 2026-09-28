def bubble_sort(list1):

    # Outer loop for traversing the entire list
    for i in range(len(list1) - 1):

        # Inner loop for comparing adjacent elements
        for j in range(len(list1) - 1 - i):

            # Swap if the current element is greater than the next element
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    return list1


# Main program

list1 = [5,88,94,73,99,100]

print("The unsorted list is:", list1)

# Calling the bubble sort function
print("The sorted list is:", bubble_sort(list1))
