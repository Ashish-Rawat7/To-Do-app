def task():
    tasks = []
    print("-----Welcome to To-Do list Manager!-----")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"today's task are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"task{add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"updated task {up}")
            
        elif operation == 3:
            del_val = input("Which task yuo want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"task{del_val} has been deleted...")
        
        elif operation == 4:
            print(f"total task = {tasks}")

        elif operation == 5:
            print("closing the program...")
            break

        else:
            print("invalid input")

task()