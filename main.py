import os
from dotenv import load_dotenv

adminMode = input("Are you an admin? (y/n): ")

load_dotenv()
ADMINPASSWORD = os.getenv("TASKMANAGERADMINPASSWORD")

if adminMode.lower() == "y":
    authentication = input("Enter the password: ")
    if authentication == ADMINPASSWORD:
        print("Admin mode activated.")
    else:
        print("Access denied. password is incorrect.")
    
elif adminMode.lower() == "n":
    username = input("Please enter your name: ")

    print(f"Welcome {username}!")

    from tasks import userTasks

    print("\n================ Your Tasks ================\n")


    for task in userTasks:
        print(f"- Name: {task["name"].title()}\n- Status: {task["status"].title()}\n- Priority: {task["priority"].title()}\n- Description: {task["description"]}")
        if task != userTasks[-1]:
            print("\n---\n")

    with open(r"C:\Users\DELL\Documents\Programming - Projects\Python - Projects\Practices\personal_task_manager\tasks.txt", "a") as file:
        for task in userTasks:
            file.write(f"- Name: {task["name"].title()}\n- Status: {task["status"].title()}\n- Priority: {task["priority"].title()}\n- Description: {task["description"]}")
            file.write("\n---\n")