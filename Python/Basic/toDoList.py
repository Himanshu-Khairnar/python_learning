task = []

while True:

    def addTasK():
        tasks = input("Enter your Task: ")
        task.append(tasks)
        print(f"task {tasks} appended successfully\n")
        print("-" * 40)

    def completeTask():
        showTask()
        taskNumber = int(input("Enter the index you wanna delete: "))
        task.pop(taskNumber)

    def showTask():

        for index, item in enumerate(task):
            print(f"{index}. {item} \n")
            print("-" * 40)

    choice = int(
        input(
            "1. Add Task\n2. Complete Task\n3. Show Task\n4. Exit\nEnter your choice: "
        )
    )
    print("-" * 40)
    if choice == 1:
        addTasK()
    elif choice == 2:
        completeTask()
    elif choice == 3:
        showTask()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")  
        