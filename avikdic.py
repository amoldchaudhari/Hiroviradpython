students = []
#taking student numbers
num_students = int(input("Enter the number of students "))

#for loop - to collect the data of the students
for i in range(num_students):
    print("Enter the details of the student ", (i+1), ":")

    student = {}  #dictionary

    student['name'] = input("Enter the student name ")
    student['marks'] = int(input("Enter the marks "))  #float()

    students.append(student)


print(students)


print("Summary of all the students ")


#for- loop - printing the student details
for i in range(num_students):
    student_display = students[i]
    print("Student ", (i+1))
    print("Name is :- ", (student_display['name']))
    print("Mark is :- ", (student_display['marks']))