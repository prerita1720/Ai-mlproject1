# prerita collection maniupulator 

print(" Welcome to Student Data Organizer ")

students = []  

while True:
    print("===== Menu =====")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    print("================")

    choice = input("Enter your choice (1-6): ")

    # 1
    if choice == "1":
        student = {}
        student["id"] = input("Enter Student ID: ")
        student["name"] = input("Enter Name: ")
        student["age"] = int(input("Enter Age: "))
        student["grade"] = input("Enter Grade: ")
        student["subjects"] = set(input("Enter Subjects :"))
        students.append(student)
        print("Student added!")

    # 2
    elif choice == "2":
        print("--- All Students ---")
        if students:  
            i = 0
            for student in students:
                print(f"Student {i}")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Grade:", student["grade"])
                print("Subjects:", end=" ")
                for sub in student["subjects"]:
                    print(sub, end=" ")
                print()
                i += 1
        else:
            print("No students found.")

   
 # 3
    elif choice == "3":
        num = int(input("Enter student number to update : "))
        students =    int(input("New Age: "))
        students  = input("New Grade: ")
        students = set(input("New Subjects : "))
        print(" Student updated!")

    # 4
    elif choice == "4":
        num = int(input("Enter student number to delete : "))
        del students
        print(" Student deleted!")


    # 5 
    elif choice == "5":
        print("--- Subjects Offered ---")
        all_subjects = set()
        for student in students:
            all_subjects.update(student["subjects"])
        if all_subjects:
            print("Subjects Offered:", end=" ")
            for sub in all_subjects:
                print("-", all_subjects)
            print()
        else:
            print("No subjects found.")

    #6

            

    elif choice == "6":
        print(" Thank you for using Student Data Organizer!")
        break

    else:
        print(" Please enter a valid option (1-6).")
