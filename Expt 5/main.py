FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("\n--- Task List ---")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Sort Tasks")
        print("5. Show All Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print("Task added.")

        elif choice == '2':
            display_tasks(tasks)
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

        elif choice == '3':
            display_tasks(tasks)
            task_num = int(input("Enter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_num - 1] = new_task
                print("Task updated.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            tasks.sort()
            print("Tasks sorted alphabetically.")

        elif choice == '5':
            display_tasks(tasks)

        elif choice == '6':
            save_tasks(tasks)
            print("Tasks saved to file. Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    
    print("\nFinal tasks stored as tuple:")
    task_tuple = tuple(tasks)
    for i, task in enumerate(task_tuple, start=1):
        print(f"{i}. {task}")

main()
