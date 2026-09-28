def s_sort(a):
    for i in range(len(a)):
        least = i

        for k in range(i + 1, len(a)):
            if a[k] < a[least]:
                least = k

        # Swap the found minimum element with the first element
        swap(a, least, i)


def swap(a, least, i):
    temp = a[least]
    a[least] = a[i]
    a[i] = temp


print("Enter elements into list:")

a = [int(x) for x in input().split()]

s_sort(a)

print("The sorted list is:", a)
