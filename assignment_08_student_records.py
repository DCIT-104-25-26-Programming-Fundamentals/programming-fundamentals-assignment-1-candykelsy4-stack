def print_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")

def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)

def add_student(students):
    name = input("Student name: ").strip()
    student_id = int(input("Student ID: "))
    count = int(input("How many scores? "))
    scores = []
    for i in range(1, count + 1):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)
    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')

def display_all_students(students):
    if not students:
        print("No students have been added yet.")
        return
    print("-" * 60)
    print(f"{'Name':<20} {'ID':<12} {'Scores':<20} {'Average'}")
    print("-" * 60)
    for s in students:
        scores_str = ", ".join(str(int(sc) if sc == int(sc) else sc) for sc in s["scores"])
        avg = calculate_average(s["scores"])
        print(f"{s['name']:<20} {s['id']:<12} {scores_str:<20} {avg}")
    print("-" * 60)

def calculate_student_average(students):
    student_id = int(input("Enter student ID: "))
    for s in students:
        if s["id"] == student_id:
            avg = calculate_average(s["scores"])
            print(f"{s['name']}'s average score: {avg}")
            return
    print("Error: Student ID not found.")

def main():
    students = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")

main()