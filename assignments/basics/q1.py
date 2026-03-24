'''1. If the marks obtained by a student in five different subjects are input through the keyboard, find
out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''

sub1 = int(input("Enter 1st value= "))
sub2 = int(input("Enter 2nd value= "))
sub3 = int(input("Enter 3rd value= "))
sub4 = int(input("Enter 4th value= "))
sub5 = int(input("Enter 5th value= "))

# Aggreagte marks
agg_marks = sub1 + sub2 + sub3 + sub4 + sub5
print("Aggregate marks = ", agg_marks)

# Percentabge
percentage = int((agg_marks/500)*100)
print("Percentage = ", percentage)
