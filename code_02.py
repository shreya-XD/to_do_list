#Simple To-Do List Application

#Features:
#1. Add Tasks
#2. View Tasks
#3. Mark Task As Completed
#4. Delete Task
#5. Exit Program

tasks=[] #pending tasks
completed=[] #completed tasks

def add_task():
    task=input('Enter a new task:').strip()
    if task =='':
        print('task cannot be empty.\n')
    else:
        tasks.append(task)
        print('Task added!\n')

def view_tasks():
    for task in tasks:print('\n---TO-DO LIST---')
    print('\n pending tasks:')
    if len(tasks)==0:
        print('No pending tasks.\n')
    else:
        for i, task in enumerate(tasks, 1):
            print(f'{i}.{task}')
    print('\n completed tasks:')
    if len(completed)==0:
        print('No completed tasks.\n')
    else:
        for i, task in enumerate(completed, 1):
            print(f'{i}.{task}')
    print()

def mark_completed():
    if len(tasks)==0:
        print('no tasks available.\n')
        return

    view_tasks()
    try:
        number=int(input('Enter task number to mark complete:'))
        if 1<=number<=len(tasks):
            finished=tasks.pop(number-1)
            completed.append(finished)
            print('Task marked as complete!\n')
        else:
            print('Invalid task number.\n')
    except ValueError:
        print('Please enter a valid number.\n')

def delete_task():
    if len(tasks)==0:
        print('No tasks to delete.\n')
        return
    view_tasks()
    try:
        number=int(input('Enter task number to delete:'))
        if 1<=number<=len(tasks):
            removed=tasks.pop(number-1)
            print(f'task {removed} has been deleted.\n')
        else:
            print('Invalid task number.\n')
    except ValueError:
        print('Please enter a valid number.\n')

def main_menu():
    while True:
        print('---TO-DO LIST MENU---')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Mark Completed')
        print('4. Delete Task')
        print('5. Exit')

        choice=input('Enter your choice:')

        if choice=='1':
            add_task()
        elif choice=='2':
            view_tasks()
        elif choice=='3':
            mark_completed()
        elif choice=='4':
            delete_task()
        elif choice=='5':
            print('Thank You.\n')
            break
        else:
            print('Invalid choice.\n')

main_menu()



