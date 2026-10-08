queue=[]
size=int(input("Enter the size of the queue:"))
while True:

    print(" \nQueue Menu:")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    choice=int(input("Enter your choice form 1-5:"))
    if choice==1:
        
        if len(queue)==size:
            print("Queue is full.Cant add elements into the queue")

        else:
            value=int(input("Enter the value to be added into the queue:"))
            queue.append(value)
            print("Value inserted")
 
    elif choice==2:
        if len(queue)==0:
            print("There are no elements to delete in the queue")

        else:
            value=queue.pop(0)
            print("Value deleted:",value)
 
    elif choice==3:
        if len(queue)==0:
            print("There are no elements no print in the queue")
        else:
            print("First element is:",queue[0])
 
    elif choice==4:
        if len(queue)==0:
            print("There are no elements to display")

        else:
            print("Queue:",queue)
 
    elif choice==5:
        print("Exiting...")
        break
 
    else:
        print("invalid choice")
  
 
