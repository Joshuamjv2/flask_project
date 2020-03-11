from flask import Flask, render_template, url_for
app  = Flask(__name__)

name = ''
course = ''
subjects_offered = ''.split( )
grades = []
gp_ponint = 0
sub_point = 0
qualify = True

grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}

courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']
subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                            courses[1]:['Physics', 'Chemistry', 'Biology', 'Math'],
                            courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                            courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry'],
                            courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}

def subject_valid():
    for i in subjects_offered:
        if i in courses < 2:
            print('You do not have the required subjects to do this course.')

#list database for given data
store_details = {}

#print(courses[0])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
