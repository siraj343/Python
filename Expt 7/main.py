def display_records(records):
    if not records:
        print("No student records available.")
    else:
        print("\n--- Student Records ---")
        for name, data in records.items():
            print(f"Name: {name}, Grade: {data['grade']}, Attendance: {data['attendance']}%")

def main():
    student_records = {}

    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Update Attendance")
        print("4. Remove Student")
        print("5. View All Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in student_records:
                print("Student already exists.")
            else:
                grade = input("Enter grade: ")
                attendance = float(input("Enter attendance (%): "))
                student_records[name] = {"grade": grade, "attendance": attendance}
                print("Student added.")

        elif choice == '2':
            name = input("Enter student name to update grade: ")
            if name in student_records:
                new_grade = input("Enter new grade: ")
                student_records[name]["grade"] = new_grade
                print("Grade updated.")
            else:
                print("Student not found.")

        elif choice == '3':
            name = input("Enter student name to update attendance: ")
            if name in student_records:
                new_attendance = float(input("Enter new attendance (%): "))
                student_records[name]["attendance"] = new_attendance
                print("Attendance updated.")
            else:
                print("Student not found.")

        elif choice == '4':
            name = input("Enter student name to remove: ")
            if name in student_records:
                del student_records[name]
                print("Student removed.")
            else:
                print("Student not found.")

        elif choice == '5':
            display_records(student_records)

        elif choice == '6':
            print("Exiting Student Record Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()
