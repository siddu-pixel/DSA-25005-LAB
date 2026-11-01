
class BinaryTree:
    def __init__(self):
        self.tree = []

    # Insertion
    def insert(self, data):
        self.tree.append(data)
        print(data, "inserted successfully")

    # Searching
    def search(self, key):
        if key in self.tree:
            print("Element found at position", self.tree.index(key))
        else:
            print("Element not found")

    # Deletion
    def delete(self, key):
        if key not in self.tree:
            print("Element not found")
            return

        index = self.tree.index(key)
        last = self.tree.pop()

        if index < len(self.tree):
            self.tree[index] = last

        print(key, "deleted successfully")

    # Inorder Traversal
    def inorder(self, i=0):
        if i < len(self.tree):
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    # Preorder Traversal
    def preorder(self, i=0):
        if i < len(self.tree):
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    # Postorder Traversal
    def postorder(self, i=0):
        if i < len(self.tree):
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")

    # Display
    def display(self):
        if not self.tree:
            print("Tree is empty")
        else:
            print("Binary Tree:", self.tree)


# Main program
bt = BinaryTree()

while True:
    print("\n--- BINARY TREE USING ARRAY ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Display")
    print("7. Searching")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter element: "))
        bt.insert(data)

    elif ch == 2:
        data = int(input("Enter element to delete: "))
        bt.delete(data)

    elif ch == 3:
        print("Inorder:")
        bt.inorder()
        print()

    elif ch == 4:
        print("Preorder:")
        bt.preorder()
        print()

    elif ch == 5:
        print("Postorder:")
        bt.postorder()
        print()

    elif ch == 6:
        bt.display()

    elif ch == 7:
        key = int(input("Enter element to search: "))
        bt.search(key)

    elif ch == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
