
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Insertion
    def insert(self, key):
        index = key % self.size

        temp = self.table[index]

        while temp:
            if temp.data == key:
                print("Duplicate element")
                return
            temp = temp.next

        new_node = Node(key)
        new_node.next = self.table[index]
        self.table[index] = new_node

        print("Element inserted successfully")

    # Searching
    def search(self, key):
        index = key % self.size
        temp = self.table[index]

        while temp:
            if temp.data == key:
                print("Element found at index", index)
                return

            temp = temp.next

        print("Element not found")

    # Deletion
    def delete(self, key):
        index = key % self.size
        temp = self.table[index]
        prev = None

        while temp:
            if temp.data == key:

                if prev is None:
                    self.table[index] = temp.next
                else:
                    prev.next = temp.next

                print("Element deleted successfully")
                return

            prev = temp
            temp = temp.next

        print("Element not found")

    # Display
    def display(self):
        print("\nHash Table:")

        for i in range(self.size):
            print(i, end=" -> ")

            temp = self.table[i]

            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")


# Main Program
size = int(input("Enter hash table size: "))
h = HashTable(size)

while True:
    print("\n--- HASHING USING LINKED LIST ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        h.insert(key)

    elif ch == 2:
        key = int(input("Enter key to search: "))
        h.search(key)

    elif ch == 3:
        key = int(input("Enter key to delete: "))
        h.delete(key)

    elif ch == 4:
        h.display()

    elif ch == 5:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
