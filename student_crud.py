students = {}

def create_student():
    sid = input("Enter new student ID: ")
    if sid in students:
        print("ID already exists.")
        return
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    students[sid] = {"name": name, "age": age, "grade": grade}
    print("Student created.\n")

def read_student():
    sid = input("Enter student ID to view: ")
    record = students.get(sid)
    if record:
        print(f"ID: {sid}, Name: {record['name']}, Age: {record['age']}, Grade: {record['grade']}\n")
    else:
        print("No record found.\n")

def update_student():
    sid = input("Enter student ID to update: ")
    if sid not in students:
        print("No record found.")
        return
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    grade = input("Enter new grade: ")
    students[sid].update({"name": name, "age": age, "grade": grade})
    print("Student updated.\n")
def delete_student():
    sid = input("Enter student ID to delete: ")
    if students.pop(sid, None):
        print("Student deleted.\n")
    else:
        print("No record found.\n")
def list_students():
    if not students:
        print("No students in record.\n")
        return
    for sid, info in students.items():
        print(f"{sid}: {info}")
    print()
# Menu loop
while True:
    print("1) Create  2) Read  3) Update  4) Delete  5) List All  6) Exit")
    choice = input("Select option: ")
    if choice == '1':
        create_student()
    elif choice == '2':
        read_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        list_students()
    elif choice == '6':
        print("Exiting.")
        break
    else:
        print("Invalid choice.\n")