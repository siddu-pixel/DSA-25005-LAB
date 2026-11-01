
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    # Get height
    def height(self, root):
        if root is None:
            return 0
        return root.height

    # Get balance factor
    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left),
                          self.height(y.right))

        x.height = 1 + max(self.height(x.left),
                          self.height(x.right))

        return x

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left),
                          self.height(x.right))

        y.height = 1 + max(self.height(y.left),
                          self.height(y.right))

        return y

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

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        bf = self.balance(root)

        # LL Case
        if bf > 1 and data < root.left.data:
            return self.right_rotate(root)

        # RR Case
        if bf < -1 and data > root.right.data:
            return self.left_rotate(root)

        # LR Case
        if bf > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if bf < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find minimum node
    def min_value(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp

    # Deletion
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        bf = self.balance(root)

        # LL Case
        if bf > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if bf > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if bf < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if bf < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

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
avl = AVLTree()
root = None

while True:
    print("\n--- AVL TREE OPERATIONS ---")
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
        root = avl.insert(root, data)
        print("Element inserted successfully")

    elif ch == 2:
        data = int(input("Enter element to delete: "))

        if avl.search(root, data):
            root = avl.delete(root, data)
            print("Element deleted successfully")
        else:
            print("Element not found")

    elif ch == 3:
        key = int(input("Enter element to search: "))

        if avl.search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif ch == 4:
        print("Inorder Traversal:")
        avl.inorder(root)
        print()

    elif ch == 5:
        print("Preorder Traversal:")
        avl.preorder(root)
        print()

    elif ch == 6:
        print("Postorder Traversal:")
        avl.postorder(root)
        print()

    elif ch == 7:
        print("AVL Tree:")
        avl.display(root)

    elif ch == 8:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
