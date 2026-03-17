# Student Record Management System

# List to store student records
students = []

def add_student(name, age, grade):
    """
    Adds a new student record to the list.
    """
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)


def display_students():
    """
    Displays all student records.
    """
    print("\nStudent Records:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")


def find_student(name):
    """
    Searches for a student by name.
    """
    for student in students:
        if student["name"] == name:
            print("\nStudent Found:")
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    
    print("\nStudent not found.")


def main():
    """
    Main function to run the program.
    """
    add_student("Ali", 20, "A")
    add_student("Sara", 21, "B")

    display_students()
    find_student("Ali")


# Run the program
main()