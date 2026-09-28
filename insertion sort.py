def insertion_sort(list1):

    # Outer loop to traverse through the list
    for i in range(1, len(list1)):

        value = list1[i]

        # Move elements greater than value one position ahead
        j = i - 1

        while j >= 0 and value < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1

        list1[j + 1] = value

    return list1


# Main program

list1 = [10, 5, 13, 8, 2]

print("The unsorted list is:", list1)

print("The sorted list is:", insertion_sort(list1))
