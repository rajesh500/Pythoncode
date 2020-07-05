student_list={"Rajesh":[150,200,165,109,120,115,98], "Jak":[145,103,120,112,106,165,175], "Rakesh":[135, 106, 117, 118, 119, 150, 135] }
subjects=["English", "Maths","Physics", "Chemistry", "Computers", "Program"]
highest_marks={}
student_list_keys=[]
student_list_values=[]
total_marks={}
marks=0
c=1
for i in student_list.keys():
    student_list_keys.append(i)
print(student_list_keys)

k=input("please enter student name:")
for k in student_list_keys:
    # if k in student_list_keys:
    values= student_list[k]
    for j in range(len(values)):
        marks=marks+values[j]
total_marks.setdefault(k, marks)
m=0
for l, n in total_marks.items():
    if n>m:
        m=n
if n==m:
    print(l, "is the 1st ranker in class with marks",  m, '/ 1725')





indvd_view=input("would you like to view student marks, please enter yes or no : ")
if indvd_view=='yes':
    user_name = input("Enter student name : ")
    if user_name in student_list_keys:
        indvd_marks = student_list[user_name]
        for i in range(len(indvd_marks) - 1):
            print(subjects[i], "Marks is", indvd_marks[i])
    else:
        print("Enter name is not in Database")
# elif indvd_view != 'yes':
#     print("Enter name is not in Database")
else:
    print("Thank you!")

