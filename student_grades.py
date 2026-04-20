students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. Show All")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        grade = input("Enter grade: ")
        students[name] = grade

    elif choice == "2":
        name = input("Enter name to update: ")
        if name in students:
            students[name] = input("Enter new grade: ")
        else:
            print("Student not found!")

    elif choice == "3":
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
