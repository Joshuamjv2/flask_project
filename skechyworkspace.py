#supposed to be in the form
#print('please fill the form below as requires')
#name = input('Course: ')
#done_subjects = input('Subjects)
#grades = input('GRADES')

#course = input('Course: ')

grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}

#Dealing with courses and subjects
courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']
subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[1]:['Physics', 'Chemistry', 'Biology', 'Math'],
                        courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                        courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry'],
                        courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}
store_details = {}

#print(courses[0])

store_details = {'name: ':'Joshua Muwanguzi',
                "A'Level: ":'PCB/SubMath',
                'grades: ':'A, B, C 1, 3',
                'course applied for: ':'Engineering',
                'Total weights: ':45,
                'Qualified: ':'YES'}

print(store_details)
for i in store_details:
    print(i)