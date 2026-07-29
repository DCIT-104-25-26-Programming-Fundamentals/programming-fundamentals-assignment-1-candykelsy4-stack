def print_menu():
    print("\n============================")
    print("       TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter task: ").strip()
    tasks.append(task)
    print(f'Task added: "{task}"')

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

def delete_task(tasks):
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
    view_tasks(tasks)
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f'Task "{removed}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

main()