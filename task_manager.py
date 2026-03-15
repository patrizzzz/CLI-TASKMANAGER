task = []
donetask = []
import os
import time
import json
import subprocess
import webbrowser

def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

def remove_expired_tasks():
    current_time = time.time()
    for t in task:
        if current_time - t["created_at"] > t["expires_in"] * 24 * 3600:
            task.remove(t)
            print(f'{t["name"]} has expired and removed from the task')

def add():
    while True:
        addtask = input("Enter phrase (or 'done' to stop and back to back to main menu): ")
        if addtask == "done":
            break
        expires_in = int(input("Enter the number of days until the task expires: "))
        task.append({"name":addtask, "created_at":time.time(), "expires_in":expires_in})
        print(f'this is the task so far {addtask}, expires in {expires_in} days')

def view():
    print("\n=== Active Tasks ===")
    for i,t in enumerate(task):
        print(f'{i+1}: {t["name"]} (expires in {t["expires_in"]} days)')
    print("\n=== Completed Tasks ===")
    for i,t in enumerate(donetask):
        print(f'{i+1} [x] done: {t["name"]}')

def remove():
    if not task:
        print("No task to remove")
        return
    while True:
        view()
        user_input = input("Enter the index of the task to remove (or 'exit'/'0' to stop): ")
        if user_input.lower() == 'exit' or user_input == '0':
            return
        try:
            rm = int(user_input)
        except ValueError:
            print("Please enter a valid number or 'exit'")
            continue
        if 1 <= rm <= len(task):
            removed = task.pop(rm-1)
            print(f'{removed["name"]} is removed from the task')
        else:
            print("Invalid index")
def task_progress():
    while True:
        view()
        user_input = input("Enter the index of the task to mark done (or 'exit'/'0' to stop): ")
        if user_input.lower() == 'exit' or user_input == '0':
            return
        try:
            mark = int(user_input)
        except ValueError:
            print("Please enter a valid number or 'exit'")
            continue
        if 1 <= mark <= len(task):
            completed = task[mark-1]
            if completed in donetask:
                print("already marked as done")
            else:
                donetask.append(completed)
                task.pop(mark-1)
                print(f'{completed["name"]} marked as done')
        elif mark == -1:
            return
def save_task():
    with open('task.txt', 'w') as f:
        json.dump(task, f)
    with open('done.txt', 'w') as f:
        json.dump(donetask, f)
    print("Task saved")
def load_task():
    try:
        with open('task.txt', 'r') as f:
            content = f.read()
            if content:
                global task
                task = json.loads(content)
        with open('done.txt', 'r') as f:
            content = f.read()
            if content:
                global donetask
                donetask = json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        task = []
        donetask = []
def delete_xotext():
    try:
        with open('task.txt', 'w') as f:
            json.dump([], f)
        with open('done.txt', 'w') as f:
            json.dump([], f)
        global task, donetask
        task = []
        donetask = []
        print("Task deleted")
    except FileNotFoundError:
        pass
def funny_button():
    print("Opening YouTube video...")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    print("Closing VS Code and Task Manager...")
    time.sleep(0.5)
    os.system("kill -9 $(pgrep -f 'code')")  # Close VS Code on Linux
    clear_screen()
    exit()

def main():
    load_task()
    user = os.environ.get('USER', 'User')
    menu = [exit, add, view, remove, task_progress, save_task, delete_xotext, funny_button]
    while True:
        clear_screen()
        print(f"Welcome {user} To Task Manager\n1. Add\n2. View\n3. Remove\n4. Task Progress\n5. Save Task\n6. Delete\n7. Funny Button\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == '0':
            clear_screen()
            break
        try:
            choice = int(choice)
            if 0 <= choice < len(menu):
                clear_screen()
                menu[choice]()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")
if __name__ == "__main__":
    main()