task = []
donetask = []

def add():
    while True:
        addtask = input("Enter phrase (or 'done' to stop and back to back to main menu): ")
        if addtask == "done":
            break
        task.append(addtask)
        print(f'this is the task so far {addtask}')

def view():
        for i,t in enumerate(task):
            print(f'{i+1}: {t}')
        for i,t in enumerate(donetask):
            print(f'{i+1} [x]done: {t}')

def remove():
    if not task:
        print("No task to remove")
        return
    while True:
        view()
        rm= int(input("Enter the index of the task to remove: "))
        if 1 <= rm <=len(task):
            removed = task.pop(rm-1)
            print(f'{removed} is removed from the task')
        else:
            print("Invalid index")
            return
def task_progress():
        while True:
            view()
            mark = int(input("Enter the index of the task to mark done to stop enterinalid: "))
            if 1 <= mark <= len(task):
                completed = task[mark-1]
                if completed in donetask:
                    print("already marked as done")
                else:
                    donetask.append(completed)
                print(f'this is the task so far {completed}')
            elif mark == -1:
                return
def save_task():
    with open('task.txt', 'w') as f:
        f.write("this is my task\n")
        for i,t in enumerate(task):
            f.write(f' {t}\n')
    with open('done.txt', 'w') as f:
        f.write("this is my done task\n")
        for i,t in enumerate(donetask):
            f.write(f' [x]{t}\n')
    print("Task saved")
def load_task():
    try:
        with open('task.txt', 'r') as f:
            for line in f:
                task.append(line.strip())
        with open('done.txt', 'r') as f:
            for line in f:
                donetask.append(line.strip())
    except FileNotFoundError:
        pass
def delete_xotext():
    try:
        with open('task.txt', 'w') as f:
            f.write("")
            print("Task deleted")
        with open('done.txt', 'w') as f:
            f.write("")
    except FileNotFoundError:
        pass
def edit():
    if not task:
        print("No task to edit")
        return
    while True:
        view()
        try:
            idx = int(input("Enter the index of the task to edit (or 0 to cancel): "))
            if idx == 0:
                break
            if 1 <= idx <= len(task):
                new_desc = input("Enter new task description: ")
                task[idx-1] = new_desc
                print(f"Task {idx} updated successfully!")
                break
            else:
                print("Invalid index")
        except ValueError:
            print("Invalid input, please enter a number")
def main():
    load_task()
    while True:
        print("Welcome To Task Manager\n1. add\n2. view\n3. remove\n4. task process\n5.Save task\n6.Delete\n7.Edit Task\n0. Exit")
        menu = {
            1: add,
            2: view,
            3: remove,
            4: task_progress,
            5: save_task,
            6: delete_xotext,
            7: edit,
            0: exit
        }
        choice = int(input("Enter your choice: "))
        if choice in menu:
            menu[choice]()
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()