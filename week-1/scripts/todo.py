tasks = []

while True:

    print("--To Do List--")
    print("Add Task: Click 1")
    print("View Task: Click 2")
    print("Exit: Click 3")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("Your Tasks: ")
        
        counter = 1
        for task in tasks:
            print(counter, ".",task)
            counter += 1

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option")