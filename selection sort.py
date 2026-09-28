def selection_sort(array):

    length = len(array)

    for i in range(length - 1):

        minIndex = i

        for j in range(i + 1, length):

            if array[j] < array[minIndex]:
                minIndex = j

        # Swap the found minimum element with the first element
        array[i], array[minIndex] = array[minIndex], array[i]

    return array


# Main program

array = [26,7,40,38,12]

print("The sorted array is:", selection_sort(array))
