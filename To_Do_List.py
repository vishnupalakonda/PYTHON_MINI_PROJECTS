tasks = []
while True:
    print("\n+===========================+")
    print("|        To-Do List         |")
    print("+===========================+")
    print("|  1. Add Task              |")
    print("|  2. View Task             |")
    print("|  3. Mark as Completed     |")
    print("|  4. Delete Task           |")
    print("|  5. Exit                  |")
    print("+===========================+")
    try:
        choice = int(input("Choose a Option From 1 To 5: "))
        if choice == 1:
            print("\n+===========================+")
            print("|        Add New Task       |")
            print("+===========================+")
            new_task = input("Enter a new task: ")
            if new_task.strip() == "":
                print("Task cannot be empty!")
            else:
                tasks.append({
                    "task": new_task,
                    "completed": False
                })
                print("Task Added Successfully!")
        elif choice == 2:
            print("\n+===========================+")
            print("|         Your Tasks        |")
            print("+===========================+")
            if len(tasks) == 0:
                print("No Tasks Are Found")
            else:
                for i in range(len(tasks)):
                    if tasks[i]["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"
                    print(f"{i + 1}. {tasks[i]['task']} - {status}")
        elif choice == 3:
            print("\n+===========================+")
            print("|      Mark as Complete     |")
            print("+===========================+")
            if len(tasks) == 0:
                print("No Tasks Are Found")
            else:
                for i in range(len(tasks)):
                    status = "Completed" if tasks[i]["completed"] else "Pending"
                    print(f"{i + 1}. {tasks[i]['task']} - {status}")
                task_number = int(input("Enter Task Number to Complete: "))
                if 1 <= task_number <= len(tasks):
                    if tasks[task_number - 1]["completed"]:
                        print("Task is already completed!")
                    else:
                        tasks[task_number - 1]["completed"] = True
                        print("Task Marked as Completed!")
                else:
                    print("Invalid Task Number!")
        elif choice == 4:
            print("\n+===========================+")
            print("|        Remove Task        |")
            print("+===========================+")
            if len(tasks) == 0:
                print("No Tasks Are Found")
            else:
                for i in range(len(tasks)):
                    status = "Completed" if tasks[i]["completed"] else "Pending"
                    print(f"{i + 1}. {tasks[i]['task']} - {status}")
                task_number = int(input("Enter Task Number to Remove: "))
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"'{removed_task['task']}' Removed Successfully!")
                else:
                    print("Invalid Task Number!")
        elif choice == 5:
            print("\n+===========================+")
            print("|    Exited Successfully    |")
            print("+===========================+")
            break
        else:
            print("Invalid Choice")
            print("Please Choose Correct Choice...")
    except ValueError:
        print("Please Enter a Valid Number!")