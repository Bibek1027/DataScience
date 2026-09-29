tasks = []

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Add task
    if choice == "1":
        task = input("Enter a task: ")

        if task.strip() == "":
            print("Task cannot be empty.")
        else:
            tasks.append({
                "task": task,
                "completed": False
            })

            print("Task added!")

    # View tasks
    elif choice == "2":

        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")

            number = 1

            for task in tasks:

                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(number, ".", task["task"], "-", status)

                number += 1

    # Mark task as completed
    elif choice == "3":

        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            number = 1

            for task in tasks:
                print(number, ".", task["task"])
                number += 1

            task_number = int(input("Enter task number to complete: "))

            if task_number >= 1 and task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Delete task
    elif choice == "4":

        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            number = 1

            for task in tasks:
                print(number, ".", task["task"])
                number += 1

            task_number = int(input("Enter task number to delete: "))

            if task_number >= 1 and task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Deleted:", deleted_task["task"])
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    # Invalid option
    else:
        print("Invalid option. Please choose 1-5.")