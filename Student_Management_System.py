students = []
while True:
    print("\n+================================+")
    print("|     Student Management System  |")
    print("+================================+")
    print("|  1. Add Student                |")
    print("|  2. View Students              |")
    print("|  3. Search Student             |")
    print("|  4. Update Student             |")
    print("|  5. Delete Student             |")
    print("|  6. View All Records           |")
    print("|  7. Exit                       |")
    print("+================================+")
    try:
        choice = int(input("Choose an Option From 1 To 7: "))
        if choice == 1:
            print("\n+================================+")
            print("|          Add Student           |")
            print("+================================+")
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            course = input("Enter Student Course: ")
            marks = float(input("Enter Student Marks: "))
            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }
            students.append(student)
            print("Student Added Successfully!")
        elif choice == 2:
            print("\n+================================+")
            print("|         Student Details        |")
            print("+================================+")
            if len(students) == 0:
                print("No Students Found.")
            else:
                for student in students:
                    print(f"ID     : {student['id']}")
                    print(f"Name   : {student['name']}")
                    print(f"Age    : {student['age']}")
                    print(f"Course : {student['course']}")
                    print(f"Marks  : {student['marks']}")
                    print("--------------------------------")
        elif choice == 3:
            print("\n+================================+")
            print("|         Search Student         |")
            print("+================================+")
            search_id = input("Enter Student ID: ")
            found = False
            for student in students:
                if student["id"] == search_id:
                    print("\nStudent Found!")
                    print(f"ID     : {student['id']}")
                    print(f"Name   : {student['name']}")
                    print(f"Age    : {student['age']}")
                    print(f"Course : {student['course']}")
                    print(f"Marks  : {student['marks']}")
                    found = True
                    break
            if not found:
                print("Student Not Found!")
        elif choice == 4:
            print("\n+================================+")
            print("|         Update Student         |")
            print("+================================+")
            update_id = input("Enter Student ID: ")
            found = False
            for student in students:
                if student["id"] == update_id:
                    print("Student Found!")
                    student["name"] = input("Enter New Name: ")
                    student["age"] = int(input("Enter New Age: "))
                    student["course"] = input("Enter New Course: ")
                    student["marks"] = float(input("Enter New Marks: "))
                    print("Student Updated Successfully!")
                    found = True
                    break
            if not found:
                print("Student Not Found!")
        elif choice == 5:
            print("\n+================================+")
            print("|         Delete Student         |")
            print("+================================+")
            delete_id = input("Enter Student ID: ")
            found = False
            for student in students:
                if student["id"] == delete_id:
                    students.remove(student)
                    print("Student Deleted Successfully!")
                    found = True
                    break
            if not found:
                print("Student Not Found!")
        elif choice == 7:
            print("\n+================================+")
            print("|       Exited Successfully      |")
            print("+================================+")
            break
        elif choice == 6:
            print("\n+==================================================================+")
            print("|                     ALL STUDENT RECORDS                         |")
            print("+==================================================================+")
            if len(students) == 0:
                print("No Student Records Found.")
            else:
                print(
                    f"{'ID':<10}"
                    f"{'Name':<20}"
                    f"{'Age':<10}"
                    f"{'Course':<20}"
                    f"{'Marks':<10}"
                )
                print("-" * 70)
                for student in students:
                    print(
                        f"{student['id']:<10}"
                        f"{student['name']:<20}"
                        f"{student['age']:<10}"
                        f"{student['course']:<20}"
                        f"{student['marks']:<10}"
                    )
                print("-" * 70)
                print(f"Total Students: {len(students)}")
        else:
            print("Invalid Choice!")
            print("Please Choose Correct Choice...")
    except ValueError:
        print("Please Enter Valid Data!")