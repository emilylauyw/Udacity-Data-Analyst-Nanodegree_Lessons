"""
This prompts the user to enter names, number of missing assignments and grades.
After getting the inputs, generate a message to each of the students to remind
them of their missing assignments and grade in the class.
"""

#Ask for user input 3 times. First is to get a lis of names.
names =  input("Enter names separated by commas: ").title().split(",")
#Second, get a list of missing assignment counts.
assignment_count =  input("Enter assignment counts separated by commas: ").split(",")
# Lastly, get a list of grades.
grades =  input("Enter grades separated by commas: ").split(",")


# message string to be used for each student
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

"""
A for Loop that iterates through each set of names, assignments, and grades to
print each student's message.
The potential grade is calculated using the current grade added to two times
"""
for name, assignment_count, grade in zip(names, assignment_count, grades):
    print(message.format(name, assignment_count, grade, int(grade) + int(assignment_count)*2))
