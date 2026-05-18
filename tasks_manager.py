import os

FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def del_tasks(tasks):
    show_tasks(tasks)

    try:
        index = int(input("Enter the task number to delete :"))
        if index < 0 or index >= len(tasks):
            print("Invalid task number !")
            return
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted successfully !")
    except ValueError:
        print("Please enter a valid number !")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")
        
        match choice:
            case "1":
                show_tasks(tasks)
            case "2":
                add_task(tasks)
            case "3":
                del_tasks(tasks)
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()