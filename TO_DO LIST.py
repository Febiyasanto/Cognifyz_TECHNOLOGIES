def main():
    tasks = []
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task(s)")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == '1':
            try:
                n = int(input("How many tasks do you want to add? "))
                for i in range(n):
                    task_text = input(f"Enter task {i + 1}: ")
                    tasks.append({"task": task_text, "done": False})
                print(f"{n} task(s) added!")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '2':
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "✅" if t["done"] else "❌"
                    print(f"{i}. {t['task']} [{status}]")

        elif choice == '3':
            try:
                num = int(input("Task number to mark as done: ")) - 1
                if 0 <= num < len(tasks):
                    tasks[num]["done"] = True
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            try:
                num = int(input("Task number to update: ")) - 1
                if 0 <= num < len(tasks):
                    new_task_text = input("Enter new task text: ")
                    tasks[num]["task"] = new_task_text
                    print("Task updated!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '5':
            try:
                num = int(input("Task number to delete: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-6.")

if __name__ == "__main__":
    main()