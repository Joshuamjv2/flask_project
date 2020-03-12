courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']

subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[1]:['Physics', 'Chemistry', 'Biology', 'Math', 'Literature'],
                        courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                        courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry', 'Music'],
                        courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}

print('We offer the following courses: ')

for h in courses:
    print(h)


#Validation of prefered course: course must be present for the university
course_choice = input('Course: ')
while  course_choice not in courses:
    print('Please Choose the right course')
    course_choice = input('Course: ')


#getting course subjects
course_subjects = []
for i in subjects_for_courses:
    course_subjects = subjects_for_courses.get(course_choice)
print(course_subjects)
