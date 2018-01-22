from flask import Flask, render_template, request

from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email 
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Sh31121998!@localhost/salary_collector'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = "data"
	id = db.Column(db.Integer,primary_key = True)
	email = db.Column(db.String(120), unique= True)
	height = db.Column(db.Integer)

	def __init__(self,email,height):
		self.email =  email
		self.height = height 



@app.route('/')
def index():
	return render_template("index.html")

@app.route('/success' , methods = ['POST'])

def success():
	if request.method == 'POST':
		email = request.form["email_name"]
		salary = request.form["salary_name"]
		
		if db.session.query(Data).filter(Data.email == email).count()==0:

			data = Data(email,salary)
			db.session.add(data)
			db.session.commit()
			average_salary = db.session.query(func.avg(Data.salary))
			average_salary = round(average_salary,1)
			count = db.session.query(Data.salary).count()
			send_email(email,salary,average_salary,count)
			return render_template("success.html")

 	return render_template("index.html", text="Seems like we have gotten something from that email address already")

if __name__=="__main__":
	app.debug = True
	app.run()
