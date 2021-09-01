from flask import Flask,request,render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/resume',methods=['POST'])
def index():
    name=request.form.get('yourname')
    email=request.form.get('youremail')
    contact=request.form.get('contact')
    father_name=request.form.get('fathername')
    complete_address=request.form.get('address')
    residence_contact=request.form.get('residence')
    dob=request.form.get('dob')
    language_known=request.form.get('lang')
    graduation_college=request.form.get('gc')
    gradution_subject=request.form.get('gs')
    graduation_pass_year=request.form.get('gp')
    graduation_cgpa=request.form.get('gm')
    tenth_board=request.form.get('tb')
    tenth_subj=request.form.get('ts')
    tenth_pass=request.form.get('tp')
    tenth_marks=request.form.get('tm')
    twe_board=request.form.get('twb')
    twe_stream=request.form.get('tws')
    twe_passyear=request.form.get('twp')
    twe_marks=request.form.get('twm')
    project=request.form.get('projects')
    skill=request.form.get('skills')
    achivements=request.form.get('achievements')

    return render_template('cv.html',name=name ,email=email,contact=contact,father_name=father_name,complete_address=complete_address,
                            residence_contact=residence_contact,dob=dob,language_known=language_known,graduation_college=graduation_college,
                           gradution_subject=gradution_subject, graduation_pass_year=graduation_pass_year,graduation_cgpa=graduation_cgpa,
                           tenth_board=tenth_board,tenth_subj=tenth_subj,tenth_pass=tenth_pass,tenth_marks=tenth_marks,twe_board=twe_board,
                           twe_stream=twe_stream,twe_passyear=twe_passyear,twe_marks=twe_marks,project=project,skill=skill,
                           achivements=achivements)




   




if __name__ == '__main__':
   app.run(debug=True)
