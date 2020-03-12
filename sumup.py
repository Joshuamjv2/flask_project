import sys
#input Form for the user
applicant_name = input('Name: ')
gender = input('Gender: ').upper()
while gender != 'm'.upper() and gender != 'male'.upper() and gender != 'f'.upper() and gender != 'female'.upper():
    print("""
    Please check gender. Insert as 'M' or 'MALE' for Male,
    'F' or 'FEMALE' for Female.
    """)
    gender = input('Gender: ')

print('Please check for the course you would like to apply for.')
courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']

subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[1]:['Physics', 'Chemistry', 'Biology', 'Math', 'Literature'],
                        courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                        courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry', 'Music'],
                        courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}

print('We offer the following courses: ')

for h in courses:
    print(f'\n{h}')

#choosing course
course_choice = input('Choose Course: ')
while  course_choice not in courses:
    print('Please Choose the right course')
    course_choice = input('Choose Course: ')
opening_remarks = print(f'''
\n
Hello {applicant_name}, thanks for cosidering to apply for {course_choice} at Makerere University.
Plese provide the required information as requested below;''')
#Validation of prefered course: course must be present for the university
#subjects done in A level-subsidiary
subjects = input('UACE main 3: ').split( )
while len(subjects) != 3:
    print('Your are required to provide the major 3 subjects without subsidiary')
    subjects = input('UACE main 3(please insert a space between the subjects): ').split( )

#subjects validation: must have done 2+ subjects to qualify for a ceratin course
course_subjects = []
for i in subjects_for_courses:
    course_subjects = subjects_for_courses.get(course_choice)

considered_subjects = []

for subject in subjects:
    if subject in course_subjects:
        considered_subjects.append(subject)

while len(considered_subjects) < 2:
    print(f'''Sorry but you did not do the necessary 2 subjects required for this course.
    You can check and see which courses contain your subjects
    if you consider trying for another course.
        ''')
    check_courses = input(f'''To check courses, type y or ok and press enter.
                        If not interested, just press enter to exit. ''')
    if check_courses == 'y' or check_courses == 'ok':
        done_deal = input(f'''{subjects_for_courses}
            If you have decided on your suitable course, type yes and press enter.
            If not, just press enter to exit. ''')
        if done_deal == 'yes':
            print('Ok try again.')
        else:
            sys.exit()
    else:
        sys.exit()
    course_choice = input('Choose Course: ')
    while  course_choice not in courses:
        print('Please Choose the right course')
        course_choice = input('Choose Course: ')
    subjects = input('UACE main 3(please insert a space between the subjects): ').split( )
    while len(subjects) != 3:
        print('Your are required to provide the major 3 subjects without subsidiary')
        subjects = input('UACE main 3(please insert a space between the subjects): ').split( )
    considered_subjects = []
    for subject in subjects:
        if subject in course_subjects:
            considered_subjects.append(subject)


#while len(subject) != 3:
#subject = input('For subjects, please insert a space between each subject.\nAll three major Subjects: ').split( )
marks = input('Respective Marks for main subjects in uppercase: ').split( )
subsidiary = input('Subsidiary subject: ')
sub_mark = input('Sub-Aggregates: ')
gp = input('GP marks: ')

gp  = int(gp)
sub_mark = int(sub_mark)

gp_point = 0
sub_point = 0
gender_point = 0

#for gender point
if gender == 'F' or gender == 'FEMALE':
    gender_point = 1.5
else:
    pass

#for subsidiary
if sub_mark > 0 and sub_mark <= 6:
    sub_point = 1
elif sub_mark > 6:
    pass

#for GP
if gp > 50 and gp <= 100:
    gp_point = 1
elif gp < 50:
    pass

#grading for marks
grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}
output = ''

for ch in marks:
    output+=str(grading.get(ch))

#get individual values from output for calculations
a = int(output[0])
b = int(output[1])
c = int(output[2])

Total_points = a + b + c + gp_point + sub_point + gender_point
Total_points = float(Total_points)

#Dealong with weights
#two principal subjects for a course






















#dealing with weights fron the list
#for_weights = [a, b, c]
#for_weights.sort(reverse=True)
#top_two_for_weights = (for_weights[0]+for_weights[1])*3
#last_for_weights = (for_weights[2])*2 + gp_point + gender_point + sub_point
#total_weights_main = top_two_for_weights + last_for_weights
#total_weights_main = float(total_weights_main)






#results according to form
#print('\n')
#print('\n')
#print(f'''{applicant_name}
#Results:
#''')
#print(str(subjects[0]) + ': '+ str(marks[0]))
#print(str(subjects[1]) + ': '+ str(marks[1]))
#print(str(subjects[2]) + ': '+ str(marks[2]))
#print(subsidiary +': '+ str(sub_mark))
#print('GP: ' + str(gp))
#print('\nTotal points: ' + str(Total_points))
#print('Weights: ' + str(total_weights_main))

#if total_weights_main > 35:
 #   print(f'''
  #  Congs {applicant_name}. You qualify for the Bsc.LAW pre-entry exam.
   # You will be notified on when the exam takes place.
    #Thanks
    #MGT
    #''')
#else:
 #   print(f'''
  #  Sorry {applicant_name}. Your results don't match the expected results to enable you to do this course.
   # Our Team will contact you about some other courses we would recommend for you.
   # Thanks
   # MGT
    #''')