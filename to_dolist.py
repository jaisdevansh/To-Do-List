def task():
    tasks = []  # Empty list for addition or deletion of data
    print("__WELCOME TO do list  __")
    
    # Prompt for the number of tasks
    totaltask = int(input("Enter the number of tasks: "))
    
    # Adding initial tasks
    for i in range(1, totaltask + 1):
        taskname = input(f"Enter the task {i}: ")
        tasks.append(taskname)
    
    # Display initial tasks
    print(f"Today's tasks are: {tasks}")
    
    # Loop to manage tasks
    while True:
        operation = int(input("Enter the number:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\n"))
        
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Your task '{add}' added successfully.")
        
        elif operation == 2:
            updateval = input("Enter the task you want to update: ")
            if updateval in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updateval)
                tasks[ind] = up
                print(f"Updated task: {up}")
            else:
                print(f"Task '{updateval}' not found.")
        
        elif operation == 3:
            delval = input("Enter the task you want to delete: ")
            if delval in tasks:
                tasks.remove(delval)
                print(f"Task '{delval}' deleted successfully.")
            else:
                print(f"Task '{delval}' not found.")
        
        elif operation == 4:
            print(f"Total tasks: {tasks}")
        
        elif operation == 5:
            print("The app has been closed.")
            break
        
        else:
            print("Invalid input. Please try again.")

# Call the task function
task()
