from functools import reduce

student = {"Himanshu": 90}
while True:

    def addData(name, marks):
        student[name] = marks
        print(f"Student {name} added in the dictionary")
        print("-" * 40)

    def listData():
        for i in student:
            print(f"Student: {i}, marks:{student[i]}\n")
            print("-" * 40)

    def viewStats():
        marks = student.values()
        average = reduce(lambda x, y: x + y, marks) / len(marks)
        highest = max(marks)
        lowest = min(marks)
        print(
            f"Average marks is {average}, highest marks is {highest}, lowest marks is {lowest}"
        )
        print("-" * 40)

    choice = int(
        input(
            "1. Add Student\n2. List Students\n3. View Stats\n4. Exit\nEnter your choice: "
        )
    )
    print("-" * 40)

    if choice == 1:
        name = input("Enter the name of the student: ")
        marks = int(input("Enter the marks of the student: "))
        addData(name, marks)
    elif choice == 2:
        listData()
    elif choice == 3:
        viewStats()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
