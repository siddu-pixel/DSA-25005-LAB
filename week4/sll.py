class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at a specific position
    # Position starts from 1
    def insert_middle(self, data, position):
        if position <= 0:
            print("Invalid position")
            return

        if position == 1:
            self.insert_front(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Count number of nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    # Display linked list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# -------------------------
# Main Program
# -------------------------

ll = SinglyLinkedList()

while True:
    print("\n--- Singly Linked List ---")
    print("1. Insert at Front")
    print("2. Insert at End")
    print("3. Insert at Middle/Position")
    print("4. Delete at Beginning")
    print("5. Delete at End")
    print("6. Count")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_front(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        ll.insert_middle(data, position)

    elif choice == 4:
        ll.delete_beginning()

    elif choice == 5:
        ll.delete_end()

    elif choice == 6:
        print("Number of nodes:", ll.count())

    elif choice == 7:
        ll.display()

    elif choice == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice")



Menu-driven main program
