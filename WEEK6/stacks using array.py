# Stack implementation using Array

stack = []

while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the data: "))
        stack.append(data)
        print("Element pushed successfully")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Popped element:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
