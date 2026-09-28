# Represents the node of the list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CreateList:

    # Declaring head and tail pointers as None
    def __init__(self):
        self.head = None
        self.tail = None

    # This function will add the new node at the end of the list
    def add(self, data):

        newNode = Node(data)

        # Checks if the list is empty
        if self.head is None:

            # Both head and tail point to the new node
            self.head = newNode
            self.tail = newNode

            # Point to itself (circular)
            newNode.next = self.head

        else:

            # Tail will point to the new node
            self.tail.next = newNode

            # New node becomes the new tail
            self.tail = newNode

            # Tail points to head
            self.tail.next = self.head

    # Displays all the nodes in the list
    def display(self):

        current = self.head

        # Check if the list is empty
        if self.head is None:
            print("List is empty")
            return

        print("Nodes of the circular linked list:", end=" ")

        # Print the first node
        print(current.data, end=" ")

        # Traverse until we reach the head again
        while current.next != self.head:
            current = current.next
            print(current.data, end=" ")

        print()


# Main program

if __name__ == '__main__':

    cl = CreateList()

    # Add data to the list
    cl.add(1)
    cl.add(2)
    cl.add(3)
    cl.add(4)

    # Display all the nodes
    cl.display()
