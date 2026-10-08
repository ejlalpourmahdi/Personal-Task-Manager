username = input("Please enter your name: ")

from tasks import userTasks

print(f"Welcome {username}!")

print("\n================ Your Tasks ================\n")

for task in userTasks:
    print(f"- Name: {task["name"].title()}\n- Status: {task["status"].title()}\n- Description: {task["description"]}")
    if task != userTasks[-1]:
        print("\n---\n")