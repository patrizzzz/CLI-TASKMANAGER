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
            print(f'{i+1}: {t}')
        donesee = input("Enter phrase (or 'done' to stop and back to main menu): ")
        if donesee == "done":
            return

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
            if 0 <= mark < len(task):
                completed = task[mark]
                donetask.append(completed)
                print(f'this is the task so far {completed}')
            elif mark == -1:
                return



while True:
    print("1. Add task\n2. View task\n3. Remove task\n4.markdone")
    num = int(input("Enter your choice: "))
    if num == 1:
        add()
    elif num == 2:
        view()
    elif num == 3:
        remove()
    elif num == 4:
        task_progress()
