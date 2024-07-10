def task():
    tasks=[] #empty list
    print("------ WELCOME TO TASK MANAGEMENT APP -----")
    
    # enter total no of task
    total_task=int(input("Enter how many task you want to add :: "))
    # because of starting 1 thats why total_task +1 otherwise total_task
    for i in range (1,total_task+1): 
        task_name=input(f"Enter Task {i} :: ")
        tasks.append(task_name)
        
    print(f"Today's tasks are \n{tasks} ")
    
    while True:
        operation=int(input("Enter 1-Add\nEnter 2-Update\nEnter 3-Delete\nEnter 4-View\nEnter 5-Exit"))
        if operation==1:
            add=input("Enter task you want to add :: ")
            tasks.append(add)
            print(f"Your {add} task has been successfully added...")
            
        elif operation==2:
            # enter value to update
            update_value=input("Enter the task name you want to update :: ")
            # check the value in tasks list??
            if update_value in tasks:
                up=input("Enter new task :: ")
                # remove old task
                ind=tasks.index(update_value)
                # update old task with new task
                tasks[ind]=up
                print(f"Updated task is {up} is successfully updated...")
                