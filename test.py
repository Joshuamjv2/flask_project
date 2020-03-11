courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']

subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[1]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                        courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry'],
                        courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}

print('We offer the following courses: ')

for h in courses:
    print(h)

#Validation of prefered course
course_choice = input('Course: ')
while  course_choice not in courses:
    print('Please Choose the right course')
    course_choice = input('Course: ')

#UACE subjects
subjects = input('Subjects: ').split( )

#Course qualification logic: one must have done in A'level morethan one subject as required by a specific course
subs_in_course = ''

for item in subjects_for_courses:
    if course_choice == item:
        print(f'Hooooray {item}')
 #       for qualification_subjects in subjects:
#            subs_in_course+=item(qualification_subjects)

#print(subs_in_course)


#print(course_choice)
