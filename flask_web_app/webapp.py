from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

#dbconn = pymysql.connect('54.172.10.211', 'sufian', 'password', 'demodb')

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/submit', methods=["POST","GET"])
def submit():
	#form = request.form
	if request.method=="POST":
		print(request.form)
		fn = request.form['first']
		ln = request.form['last']
		try:
			f = request.files['filename']
			f.save(f.filename)
		except:
			pass
		dbconn = pymysql.connect('54.172.10.211', 'sufian', 'password', 'demodb')
		curs = dbconn.cursor()
		curs.execute("""INSERT INTO demo values("%s","%s")"""%(fn, ln))
		dbconn.commit()
		dbconn.close()
		return "File stored in the directory of this python program successfully!"
	return "Hi there"

@app.route('/fetch')
def fetch():
	dbconn = pymysql.connect('54.172.10.211', 'sufian', 'password', 'demodb')
	curs = dbconn.cursor()
	curs.execute("SELECT * FROM demo")
	values = curs.fetchall()
	dbconn.close()
	print(values)
	return render_template("fetch.html", result=values)
	


if __name__ == '__main__':
	app.run(debug=True)
