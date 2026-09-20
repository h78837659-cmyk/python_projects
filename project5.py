def task():
    tasks = []
    print('-----WELCOME TO THE TASK MANAGEMENT APP------')

    total_task = int(input('Enter how many tasks you want to add :-'))
    for i in range(1,total_task+1):
        task_name = input(f'Enter task {i} = ')
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("enter\n1-add\n2-update\n3-delete\n4-view\n5-exit/stop/\n"))
        if operation == 1:
            add = input('enter task you want to add = ')
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
        elif operation == 2:
          updated_val = input("Enter the task name you want to update = ")      
          if updated_val in tasks:
              up = input('Enter the new task = ')
              ind = tasks.index(updated_val)
              tasks[ind] = up
              print(f'Updated task {up}')
        elif operation == 3:
            del_val = input("which task you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f'Task {del_val} has been deleted...')
        elif operation == 4:
            print(f'Total tasks = {tasks}')
        elif operation == 5:
            print("closing the program...\nThankyou\n")
            break 
        else:
            print('Invalid input')

task()                      