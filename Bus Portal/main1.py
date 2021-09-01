from flask.templating import render_template_string
from model1 import *
from flask import Flask, render_template,request, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():

    table_data = Emp_Details.select().dicts()
    SR = False

    # * Handle CRUD Here
    if request.method == "POST":
        print(request.form.to_dict())
        if "Create" in request.form.keys():
            print("Create DB")
            Emp_Details.create(emp_id=request.form.get('emp_id'),
                               username=request.form.get('username'),
                               fromroute=request.form.get('fromroute'),
                               toroute=request.form.get('toroute'))
        
        elif "Update" in request.form.keys():
            print("Update DB")
            emp_ID = request.form.get('emp_id')
            query = Emp_Details.update(emp_id=request.form.get('emp_id'),
                                       username=request.form.get('username'),
                                       fromroute=request.form.get('fromroute'),
                                       toroute=request.form.get('toroute')).where(Emp_Details.emp_id ==emp_ID)
            n = query.execute()

        elif "Delete" in request.form.keys():
            print("Delete DB")
            emp_ID = request.form.get('emp_id')
            Emp_Details.delete().where(Emp_Details.emp_id == emp_ID).execute()

        elif "Truncate" in request.form.keys():
            print("Truncate DB")
            Emp_Details.truncate_table()

        elif "Search" in request.form.keys():
            print("Search")
            SR = True
            (request.form.to_dict())
            # query=Emp_Details.select().where(Emp_Details.emp_id == emp_ID).dicts()
            query = ""
            for i in Emp_Details.select().where(Emp_Details.emp_id == request.form.get("s_eid")).dicts():
                query = i
                print(query)

            return render_template('index.html', data=table_data, search_result = SR, search_dict_result= query)

        elif "overtime" in request.form.keys():
            return redirect(url_for('late'))

    return render_template('index.html', data=table_data, search_result = SR)


@app.route('/late',methods=['GET','POST'])
def late():
    table=Late_Sitting.select().dicts()


    if request.method == "POST":
        print(request.form.to_dict())
        if "Create" in request.form.keys():
            print("Create DB")
            Late_Sitting.create(emp_id=request.form.get('emp_id'),
                               username=request.form.get('username'),
                               dinner=request.form.get('dinner'),
                               refreshment=request.form.get('refreshment'))
        
        elif "Update" in request.form.keys():
            print("Update DB")
            emp_ID = request.form.get('emp_id')
            query = Late_Sitting.update(emp_id=request.form.get('emp_id'),
                                       username=request.form.get('username'),
                                       dinner=request.form.get('dinner'),
                                       refreshment=request.form.get('refreshment')).where(Late_Sitting.emp_id ==emp_ID)
            n = query.execute()

        elif "Delete" in request.form.keys():
            print("Delete DB")
            emp_ID = request.form.get('emp_id')
            Late_Sitting.delete().where(Late_Sitting.emp_id == emp_ID).execute()

        elif "Truncate" in request.form.keys():
            print("Truncate DB")
            Late_Sitting.truncate_table()

    return(render_template("late.html", datafield=table))





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
