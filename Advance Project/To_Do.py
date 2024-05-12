task  = []
n = int(input("Enter the number of task__"))

for i in range(1,n+1):
    to_do = input(f"Enter your {i} task : -")
    task.append(to_do)
    
while True:
    print("Enter - 1-Add: \n Enter -2-Update: \n Enter -3-Deltete:")
    choice = int(input("Enter your choice__"))
    if choice == 1:
        new_t = input("Enter new task_")
        task.append(new_t)
    elif choice == 2:
        u_t = input("Enter task to update__")
        if u_t in task:
            new_u_t  = input("Enter new task__")
            idex = task.index(u_t)
            task[idex] = new_u_t
        else:
            print("No task are here.")
    elif choice == 3:
        d_t = input("Enter task to delete__")
        if d_t in task:
            index = task.index(d_t)
            task.pop(index)
    elif choice == 0:
        break
    else:
        print("Please enter right choice")
    
    
print(f"Your all task is {task}")