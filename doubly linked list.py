# Represent a node of doubly linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:

    # Represent the head and tail of the doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # addNode() will add a node to the list
    def addNode(self, data):

        # Create a new node
        newNode = Node(data)

        # If list is empty
        if self.head is None:

            # Both head and tail will point to newNode
            self.head = self.tail = newNode

            # Head's previous will point to None
            self.head.previous = None

            # Tail's next will point to None
            self.tail.next = None

        else:

            # Add newNode after tail
            self.tail.next = newNode

            # NewNode's previous will point to tail
            newNode.previous = self.tail

            # NewNode will become the new tail
            self.tail = newNode

            # Tail's next will point to None
            self.tail.next = None

    # display() will print the nodes of the list
    def display(self):

        # Current will point to head
        current = self.head

        # Check if list is empty
        if self.head is None:
            print("List is empty")
            return

        print("Nodes of doubly linked list:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


# Create a DoublyLinkedList instance
dList = DoublyLinkedList()

# Add nodes
dList.addNode(1)
dList.addNode(2)
dList.addNode(3)
dList.addNode(4)
dList.addNode(5)

# Display the nodes
dList.display()
