file_name = "todo_list.txt"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            tasks = file.readlines()
            return [{"task": task.strip(), "completed": False} for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks():
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task["task"] + "\n")

tasks = load_tasks()

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        task_info = {"task": task, "completed": False}
        tasks.append(task_info)
        save_tasks()
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty!")

def mark_task_complete():
    incomplete_tasks = [task for task in tasks if not task["completed"]]
    if not incomplete_tasks:
        print("All tasks are already completed!")
        return
    print("\nIncomplete Tasks:")
    print("-" * 50)
    for i, task in enumerate(incomplete_tasks, start=1):
        print(f"{i}. {task['task']}")
    print("-" * 50)
    try:
        task_number = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_number <= len(incomplete_tasks):
            incomplete_tasks[task_number - 1]["completed"] = True
            save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError: 
        print("Please enter a valid number.")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    print("\nAll Tasks:")
    print("-" * 50)
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['task']} {status}")
    print("-" * 50)

def main():
    message = """
Task Manager Menu:
1 - Add Task
2 - Mark Task as Complete
3 - View All Tasks
4 - Quit
"""
    while True:
        print(message)
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_complete()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()