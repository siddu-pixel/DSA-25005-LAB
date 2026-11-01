
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            print(data, "inserted successfully")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                break
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                break
            else:
                queue.append(temp.right)

        print(data, "inserted successfully")

    # Searching
    def search(self, key):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.data == key:
                print("Element found:", key)
                return

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        print("Element not found")

    # Deletion
    def delete(self, key):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [(self.root, None)]
        target = None
        deepest = None
        parent = None

        while queue:
            temp, par = queue.pop(0)

            if temp.data == key and target is None:
                target = temp

            deepest = temp
            parent = par

            if temp.left:
                queue.append((temp.left, temp))

            if temp.right:
                queue.append((temp.right, temp))

        if target is None:
            print("Element not found")
            return

        target.data = deepest.data

        if parent is None:
            self.root = None
        elif parent.right == deepest:
            parent.right = None
        else:
            parent.left = None

        print(key, "deleted successfully")

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Display
    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        print("Binary Tree (Level Order):")

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        print()


# Main program
bt = BinaryTree()

while True:
    print("\n--- BINARY TREE USING LINKED LIST ---")
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
        bt.inorder(bt.root)
        print()

    elif ch == 4:
        print("Preorder:")
        bt.preorder(bt.root)
        print()

    elif ch == 5:
        print("Postorder:")
        bt.postorder(bt.root)
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
