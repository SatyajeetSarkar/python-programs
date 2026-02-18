'''Problem: SIT Course Fees
Siliguri Institute of Technology has started its admission process for the academic session 2026.
Admission fees vary for the different courses offered by the institute. Course fees for the
different course are given in the tabular format.
UG/PG Course Code Course Name No of
Semester

Admission
Fees+1st
semester Fees

Remaining
Semester
UG 1 BTech 8 1L 75K
UG 2 BCA 8 70K 50K
UG 3 BBA 8 70K 50K
UG 4 BHHA 6 60K 45K
UG 5 BSc 6 50K 30K
PG 6 MBA 4 1.4L 1L
PG 7 MCA 4 1.2L 80K

Surprisingly, there are scholarships available for certain categories, as listed below:
● If a student completed his/her previous degree from Techno India Group, then 10K and 15K
scholarship will be given to UG courses and PG courses for each semester and the students
will notbe eligible for any other scholarship.
● If a student has qualified the entrance test and has come through entrance test he/she willbe
eligible for 15K scholarship at thetime of admission.
● All Female candidates including TIGans will receive 10K scholarship at the time of admission.
You have to write down a function (CalculateSITcourseFees) which will take course_name, TIGans,
entrance_test, Male and systemwill return total course fees.
Course_name: coursecode is the integer value (1,2,3,4,5,6,7) and will determine the course name.
TIGans: this is integer value (1,0) determine the candidate studied his/her previous course from
TechnoIndia Group’s institute or not.
Entrance_test: this parameter indicates whether the candidate (1,0) has taken admission through
valid rank or direct.
(1,0): indicates sex of the student male or female
Example:
Input: CalculateSITcourseFees(1,1,0,1)
Output: 5,45,000.00
Explanation: Course code is 1. Student opt for BTech. TIG students will receive 10K scholarship for each
semester. 1st semester + Admission Fees=100000-10000=90000, remaining 7semester=7*(75000-
10000)=4,54000.00. Male candidate no scholarship. No scholarship for directadmission.
'''
# Fucntion to calculate SIT course fees
def CalculateSITcourseFees(course_name, TIGans, entrance_test, sex):
    # Course details
    # BTech
    if course_name == 1:     
        sems = 8
        first_fee = 100000
        remain_fee = 75000

    # BCA
    elif course_name == 2:    
        sems = 8
        first_fee = 70000
        remain_fee = 50000
    
    # BBA
    elif course_name == 3:    
        sems = 8
        first_fee = 70000
        remain_fee = 50000
    
    # BHHA
    elif course_name == 4:    
        sems = 6
        first_fee = 60000
        remain_fee = 45000

    # BSc    
    elif course_name == 5:    
        sems = 6
        first_fee = 50000
        remain_fee = 30000

    # MBA    
    elif course_name == 6:    
        sems = 4
        first_fee = 140000
        remain_fee = 100000
    
    # MCA
    elif course_name == 7:    
        sems = 4
        first_fee = 120000
        remain_fee = 80000

    else:
        print("Invalid course code")
        return

    total_fees = 0

    # Scholarships
    # Techno India Group student
    if TIGans == 1:  
        # UG course
        if course_name <= 5:   
            per_sem_scholarship = 10000
        # PG course
        else:                 
            per_sem_scholarship = 15000
        total_fees += (first_fee - per_sem_scholarship)
        total_fees += (sems - 1) * (remain_fee - per_sem_scholarship)
    else:
        total_fees += first_fee
        total_fees += (sems - 1) * remain_fee

        # Other scholarships
        if entrance_test == 1:
            total_fees -= 15000
        if sex == 0:  # female student
            total_fees -= 10000

    return f"{total_fees:,.2f}"


# Print the value
print("Output:", CalculateSITcourseFees(1, 1, 0, 1))
