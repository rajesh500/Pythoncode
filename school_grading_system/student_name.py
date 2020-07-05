# Empty list, adding marks
student_marks=[]
subjects=["English", "Maths","Physics", "Chemistry", "Computers", "Program"]
# Empty dictionary, adding keys as student_names and values as student_marks
student_list={}
# empty list, collecting student names
student_names=[]
highest_marks={}
marks=0
c=1
for i in range(c):
    nam =input("Please enter your student name:")
    for i in range(2):
        b=int(input("Enter student marks:"))
        student_marks.append(b)

# counting marks
for i in range(len(student_marks)):
    marks=student_marks[i]+marks
print(marks)


# list of marks view
# print(student_marks)

student_list[nam]=student_marks
highest_marks[nam]=marks
print(highest_marks, "Another Dictionary set")
# dictionary view student name and list of marks in all subjects
# print(student_list)


for i in student_list.keys():
    student_names.append(i)

# student name as keys view
# print(student_names)

indvd_view=input("would you like to view student marks, please enter yes or no:")
if indvd_view=='yes':
    user_name=input("Enter student name:")
    if user_name in student_names:
        indvd_marks=student_list[user_name]
        # individual marks list
        # print(indvd_marks)
        for i in range(len(indvd_marks)):
            print(subjects[i], "Marks is", indvd_marks[i])
    else:
        print("Student name is not in the Database")
else:
    print("Thank you!")