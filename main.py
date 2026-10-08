username = input("Please enter your name: ")

print(f"Welcome {username}!")

tasks = []

while True:
    print("\n================ New Task ================\n")

    taskName = input("Name: ")
    taskStatus = input("Status: ")
    taskDescription = input("Description (optional): ")

    print("\n==========================================\n")

    if taskName.strip() == "":
        print("Error! Task name can't be empty.\n")
        continue
    elif taskStatus.strip() == "":
        print("Error! Task status can't be empty.\n")
        continue
    else:
        if taskDescription == "":
            taskDescription = None

        task = {
            "name": taskName,
            "status": taskStatus,
            "description": taskDescription
        }

        tasks.append(task)

        print("Success!\n")

    repeat = input("\nDo you want to add a new task? (y/n): ")

    if repeat.lower() == "n":
        break
    elif repeat.lower() == "y":
        continue

print("\n================ Your Tasks ================\n")

for t in tasks:
    print(f"- Name: {t["name"].title()}\n- Status: {t["status"].title()}\n- Description: {t["description"]}")
    print("\n---\n")