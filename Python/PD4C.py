tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("Type 'exit' to close")

    choice = input("Enter your choice: ")

    # Exit
    if choice.lower() == "exit":
        print("To-Do List closed.")
        break

    # Add Task
    if choice == "1":
        task = input("Enter the task: ")

        if task == "":
            print("Task cannot be empty.")
            continue

        tasks.append(task)
        print("Task added successfully.")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")
            continue

        print("\nYour Tasks:")

        for number, task in enumerate(tasks, start=1):
            print(number, ".", task)

        else:
            print("All tasks displayed.")

    # Remove Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks available to remove.")
            continue

        print("\nYour Tasks:")

        for number, task in enumerate(tasks, start=1):
            print(number, ".", task)

        task_number = int(input("Enter task number to remove: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            continue

        removed_task = tasks.pop(task_number - 1)
        print("Removed:", removed_task)

    else:
        print("Invalid choice. Please try again.")