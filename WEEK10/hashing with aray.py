
class HashTable:
    DELETED = object()

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Insertion using Linear Probing
    def linear_insert(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None or self.table[pos] is self.DELETED:
                self.table[pos] = key
                print("Element inserted successfully")
                return

            if self.table[pos] == key:
                print("Duplicate element")
                return

        print("Hash table is full")

    # Insertion using Quadratic Probing
    def quadratic_insert(self, key):
        index = key % self.size

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None or self.table[pos] is self.DELETED:
                self.table[pos] = key
                print("Element inserted successfully")
                return

            if self.table[pos] == key:
                print("Duplicate element")
                return

        print("No available position")

    # Searching
    def search(self, key):
        index = key % self.size

        # Check positions using both probing sequences
        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] is not self.DELETED:
                if self.table[pos] == key:
                    print("Element found at index", pos)
                    return

        # Search using quadratic probing
        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] is not self.DELETED:
                if self.table[pos] == key:
                    print("Element found at index", pos)
                    return

        print("Element not found")

    # Deletion
    def delete(self, key):
        index = key % self.size

        # Search using both probing sequences
        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] is not self.DELETED:
                if self.table[pos] == key:
                    self.table[pos] = self.DELETED
                    print("Element deleted successfully")
                    return

        for i in range(self.size):
            pos = (index + i * i) % self.size

            if self.table[pos] is None:
                break

            if self.table[pos] is not self.DELETED:
                if self.table[pos] == key:
                    self.table[pos] = self.DELETED
                    print("Element deleted successfully")
                    return

        print("Element not found")

    # Display
    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            value = self.table[i]

            if value is None:
                print(i, ": Empty")
            elif value is self.DELETED:
                print(i, ": Deleted")
            else:
                print(i, ":", value)


# Main Program
size = int(input("Enter hash table size: "))
h = HashTable(size)

while True:
    print("\n--- HASHING USING ARRAY ---")
    print("1. Linear Probing Insertion")
    print("2. Quadratic Probing Insertion")
    print("3. Search")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        h.linear_insert(key)

    elif ch == 2:
        key = int(input("Enter key: "))
        h.quadratic_insert(key)

    elif ch == 3:
        key = int(input("Enter key to search: "))
        h.search(key)

    elif ch == 4:
        key = int(input("Enter key to delete: "))
        h.delete(key)

    elif ch == 5:
        h.display()

    elif ch == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
