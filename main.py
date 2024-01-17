from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__) 
app.secret_key='edu'                                                                     # main file

#mysql connection
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="kavimysql19@"
app.config["MYSQL_DB"]="form"
app.config["MTSQL_CURSORCLASS"]="DictCursor"
conn = MySQL(app) 

@app.route('/')                                                                          # '/' for home page
def home():                                                                              # func name can be anything home or anything
    return render_template('first.html')                                               # render_temple will take directly the templete
@app.route('/register', methods=['GET','POST'])                                                                  # table path defined
def register():                                                                          # table name
    if request.method=='POST':
        uname=request.form['sname']
        age=request.form['age']
        DOB=request.form['dob']
        phone=request.form['phone']
        mail=request.form['mail']
        gender=request.form['Gender']               #all specified in sql database
        Cpassword=request.form['fpass']
        CCpassword=request.form['lpass']
        Address=request.form['address']
        City=request.form['city']
        State=request.form['state']
        con=conn.connection.cursor()
        sql="insert into info(sname,age,dob,phone,mail,Gender,fpass,lpass,address,city,state) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        con.execute(sql,(uname,age,DOB,phone,mail,gender,Cpassword,CCpassword,Address,City,State))
        con.connection.commit()
        con.close()
        return render_template('login.html')
    return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])                                                                            
def login():
    msg=''
    if request.method=='POST':
        mail=request.form['mail']
        CCpassword=request.form['lpass']
        con=conn.connection.cursor()
        sql="select mail,lpass from info WHERE mail=%s and lpass=%s "
        result = con.execute(sql,[mail,CCpassword])
        con.connection.commit()
        con.close()
        if result:
            return render_template('recommendation.html')
        else:
            
            return render_template('login.html',msg='Incorrect Username or Password')

    return render_template('login.html')

    
     

@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/thriller')
def thriller():
    return render_template('thriller.html')

@app.route('/romcom')
def romcom():
    return render_template('romcom.html')

@app.route('/Fantasy')
def Fantasy():
    return render_template('Fantasy.html')

@app.route('/Popular')
def Popular():
    return render_template('Popular.html')

@app.route('/Poetry')
def Poetry():
    return render_template('Poetry.html')

@app.route('/fiction')
def fiction():
    return render_template('fiction.html')

@app.route('/nonfiction')
def nonfiction():
    return render_template('nonfiction.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/mystery')
def mystery():
    return render_template('mystery.html')

@app.route('/children_literature')
def children_literature():
    return render_template('children_literature.html')

@app.route('/moral')
def moral():
    return render_template('moral.html')

@app.route('/sci_fic')
def sci_fic():
    return render_template('sci_fic.html')

@app.route('/biography')
def biography():
    return render_template('biography.html')

@app.route('/novels')
def novels():
    return render_template('novels.html')

@app.route('/new_arrival')
def new_arrival():
    return render_template('new_arrival.html')



if __name__=='__main__':                                                                 # to check the 2 files are equal
    app.run(debug=True)                                                                            # to run the program