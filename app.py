from flask import Flask, render_template, url_for, redirect, request
# from Flask-WTF import Form
app  = Flask(__name__)

#print(courses[0])
@app.route('/')
@app.route('/home', methods = ['POST', 'GET'])
def home():
    subs = ['Sub-Math', 'ICT']
    courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']
    subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                                courses[1]:['Physics', 'Chemistry', 'Biology', 'Math'],
                                courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                                courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry'],
                                courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}
    pscores = ['A', 'B', 'C', 'D', 'E', 'O', 'F']
    grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}
    weights_for_courses = {courses[0]:36, courses[1]:50, courses[2]:45, courses[3]:48, courses[4]:45}
    _gender = ['Male', 'Female']
    course_choice = request.form.getlist('course_choice')
    # got = request.form.get('got')

    # course_subjects = []
    # for i in subjects_for_courses:
    #     course_subjects = subjects_for_courses.get(course_choice)
        # return course_subjects
    return render_template('home.html', subs = subs, _gender = _gender, course_choice = course_choice, courses = courses, subjects_for_courses = subjects_for_courses, pscores = pscores)



@app.route('/result', methods = ['POST', 'GET'])
def result():
    courses = ['Bsc. Engineering', 'Bsc. Medicine', 'Bsc. Law', 'Bsc. Computer Science', 'Bsc. Econ']
    subjects_for_courses = {courses[0]:['Physics', 'Chemistry', 'Biology', 'Math'],
                                courses[1]:['Physics', 'Chemistry', 'Biology', 'Math'],
                                courses[2]:['History', 'Chemistry', 'Biology', 'Math', 'ICT', 'Geography', 'Literature', 'History'],
                                courses[3]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry'],
                                courses[4]:['Math', 'Physics', 'Geography', 'Biology', 'ICT', 'Chemistry']}

    course_choice = request.form.get('course_choice')
    p1score = request.form.get('p1score')
    name = request.form.get('name')
    subsidiary = request.form.get('subsidiary')
    gender = request.form.get('gender')
    # principal3 = request.form.get('principal_3')
    # subsidiary = request.form.get('subsidiary')
    gp = request.form.get('gp')
    # final = {principal_1:'principal_1', principal_2:'principal_2', principal_3:'principal_3', subsidiary:'subsidiary', general_paper:'general_paper'}
    #ps = {principal_1:'principal_1'}
    # return render_template('result.html', form  = 'form')
    return render_template('result.html', gp = gp, gender=gender, subsidiary=subsidiary, p1score = p1score, name = name, course_choice = course_choice, courses = courses, subjects_for_courses = subjects_for_courses)# 'principal_1 = 'principal_1')

if __name__ == '__main__':
    app.run(debug=True)
