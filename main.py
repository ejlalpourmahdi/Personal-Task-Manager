username = input("Please enter your name: ")

print(f"Welcome {username}!")



while True:
    print("\n================ New Task ================\n")

    taskName = input("Name: ")
    taskStatus = input("Status: ")
    taskDescription = input("Description (optional): ")

    print("\n==========================================\n")

    if taskName.strip() == "":
        print("Error! Task name can't be empty.\n")
    elif taskStatus.strip() == "":
        print("Error! Task status can't be empty.\n")
    else:
        print("Success!")
        break