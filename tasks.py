userTasks = []
PRIORITY = ["low", "medium", "high", "emergency"]

while True:
    print("\n================ New Task ================\n")

    taskName = input("Name: ")
    taskStatus = input("Status: ")
    taskPriority = input("Priority (Low/Medium/High): ")
    taskDescription = input("Description (optional): ")

    print("\n==========================================\n")

    if taskName.strip() == "":
        print("Error! Task name can't be empty.\n")
        continue
    elif taskStatus.strip() == "":
        print("Error! Task status can't be empty.\n")
        continue
    elif taskPriority.lower() not in PRIORITY:
        print("Error! An invalid priority.\n")
        continue
    else:
        if taskDescription == "":
            taskDescription = None

        task = {
            "name": taskName,
            "status": taskStatus,
            "priority": taskPriority,
            "description": taskDescription
        }

        userTasks.append(task)

        print("Success!\n")

    repeat = input("\nDo you want to add a new task? (y/n): ")

    if repeat.lower() == "n":
        break
    elif repeat.lower() == "y":
        continue