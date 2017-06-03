from flask import Flask,render_template,request,json
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql=MySQL()
app=Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='suhas'
app.config['MYSQL_DATABASE_DB']='BucketList'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)



conn=mysql.connect()
cursor=conn.cursor()

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/showSignUp")
def showsignUp():
	return render_template('signup.html')

@app.route("/signUp",methods=['POST'])
def signUp():
	_name=request.form['inputName']
	_email=request.form['inputEmail']
	_password=request.form['inputPassword']
	_hashed_password=generate_password_hash(_password)
        cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
        data=cursor.fetchall()
	if _name and _email and _password:
		return json.dumps({'html':'<span>All fields good!!</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})




'''
if len(data) is 0:
    conn.commit()
    #return json.dumps({'message':'user created successfully!'})
else:
    #return json.dumps({'error':str(data[0])})
'''
if __name__=="__main__":
	app.run()
