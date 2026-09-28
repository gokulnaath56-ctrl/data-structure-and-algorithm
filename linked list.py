class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert a Node
def insert(root, item):
    temp = Node(item)
    temp.next = root
    return temp


# Function to display the linked list
def display(root):
    while root is not None:
        print(root.data, end=" ")
        root = root.next
    print()


# Function to convert array to linked list
def arrayToList(arr, n):
    root = None

    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])

    return root


# Main program
if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]
    n = len(arr)

    root = arrayToList(arr, n)

    display(root)
