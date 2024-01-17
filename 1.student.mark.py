def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    student_dob = input("Enter the student's date of birth: ")
    return student_id, student_name, student_dob

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course name: ")
    return course_id, course_name

def input_marks(students):
    course_id = input("Enter the course ID: ")
    marks = {}
    for student_id, _, _ in students:
        mark = float(input(f"Enter the mark for student {student_id}: "))
        marks[student_id] = mark
    return course_id, marks

def list_courses(courses):
    print("List of courses:")
    for course_id, course_name in courses.items():
        print(f"Course ID: {course_id}, Course Name: {course_name}")

def list_students(students):
    print("List of students:")
    for student_id, student_name, student_dob in students:
        print(f"Student ID: {student_id}, Name: {student_name}, DoB: {student_dob}")

def show_student_marks(course_marks):
    course_id = input("Enter the course ID: ")
    if course_id in course_marks:
        print("Student marks for the course:")
        for student_id, mark in course_marks[course_id].items():
            print(f"Student ID: {student_id}, Mark: {mark}")
    else:
        print("No marks found for the course.")

def main():
    students = []
    courses = {}
    course_marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student_info = input_student_info()
        students.append(student_info)

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_info()
        courses[course_info[0]] = course_info[1]

    while True:
        print("\n--- Menu ---")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a course")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            course_marks[input_marks(students)]
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(course_marks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()