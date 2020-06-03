from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class employee_db(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20), nullable=False)
	designation = db.Column(db.String(20),  nullable=False)
	address = db.Column(db.String(20),  nullable=False)
	phone = db.Column(db.Integer,  nullable=False)




	def __repr__(self):
		return '<display %r>' % self.name


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		add_employee = request.form['name']
		add_desigantion = request.form['designation']
		add_address = request.form['address']
		add_phone = request.form['phone']
		new_table = employee_db(name=add_employee, designation=add_desigantion, address=add_address, phone=add_phone) 

		try:
			db.session.add(new_table)
			db.session.commit()
			return redirect('/')
		except:
			return 'error!'

	else:
		display = employee_db.query.order_by(employee_db.name).all()
		return render_template('index.html', display=display)


@app.route('/search', methods=['POST', 'GET'])
def search():
	if request.method == "POST":
		query = request.form('input')
		cursor.execute("select name, designation, phone from employee_db where name like %s or designation like %s or phone like %d ",(input))
		new_table = employee_db(name=name, designation=designation, address=address,phone=phone)
		return render_template('index.html', new_table= new_table)


@app.route('/delete/<int:id>')
def delete(id):
	dele = employee_db.query.get_or_404(id)

	try:
		db.session.delete(dele)
		db.session.commit()
		return redirect('/')
	except:
		return 'error!'


if __name__ == "__main__":
	app.run(debug=True)