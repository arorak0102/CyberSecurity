# To-Do List

tasks = []

def menu():
    print("\n===== To-Do List =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def viewTasks():
    if not tasks:
        print("No tasks available!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['Title']}")

def addTask():
    title = input("Enter Task: ")
    tasks.append({"Title": title, "done": False})
    print("Task Added!")

def taskDone():
    if not tasks:
        print("No tasks available!")
        return
    viewTasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num-1]["done"] = True
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid Input!")

def deleteTask():
    if not tasks:
        print("No tasks available!")
        return
    viewTasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        print("Task Deleted!")
    except (ValueError, IndexError):
        print("Invalid Input!")

while True:
    menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        viewTasks()
    elif choice == "2":
        addTask()
    elif choice == "3":
        taskDone()
    elif choice == "4":
        deleteTask()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
