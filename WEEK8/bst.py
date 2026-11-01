
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            print("Duplicate values are not allowed")

        return root

    # Searching
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find minimum value
    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    # Deletion
    def delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Display
    def display(self, root, level=0):
        if root:
            self.display(root.right, level + 1)
            print("   " * level, root.data)
            self.display(root.left, level + 1)


# Main program
bst = BST()

while True:
    print("\n--- BINARY SEARCH TREE OPERATIONS ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Searching")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Display")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter element: "))
        bst.root = bst.insert(bst.root, data)
        print("Element inserted successfully")

    elif ch == 2:
        data = int(input("Enter element to delete: "))
        if bst.search(bst.root, data):
            bst.root = bst.delete(bst.root, data)
            print("Element deleted successfully")
        else:
            print("Element not found")

    elif ch == 3:
        key = int(input("Enter element to search: "))
        if bst.search(bst.root, key):
            print("Element found")
        else:
            print("Element not found")

    elif ch == 4:
        print("Inorder Traversal:")
        bst.inorder(bst.root)
        print()

    elif ch == 5:
        print("Preorder Traversal:")
        bst.preorder(bst.root)
        print()

    elif ch == 6:
        print("Postorder Traversal:")
        bst.postorder(bst.root)
        print()

    elif ch == 7:
        print("Binary Search Tree:")
        bst.display(bst.root)

    elif ch == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
