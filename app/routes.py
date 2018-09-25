#routes.py
from flask import render_template, request, jsonify
from app import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/add', methods=['POST'])
def add():
	addx = request.form.get('addx', type=int)
	addy = request.form.get('addy', type=int)
	try:
		result = addx + addy
	except:
		result = "Input Error"
	finally:
		return jsonify({'result' : result})

@app.route('/subtract', methods=['POST'])
def subtract():
	subx = request.form.get('subx', type=int)
	suby = request.form.get('suby', type=int)
	try:
		result = subx - suby
	except:
		result = "Input Error"
	finally:
		return jsonify({'result' : result})

@app.route('/multiply', methods=['POST'])
def multiply():
	mulx = request.form.get('mulx', type=int)
	muly = request.form.get('muly', type=int)
	try:
		result = mulx * muly
	except:
		result = "Input Error"
	finally:
		return jsonify({'result' : result})

@app.route('/divide', methods=['POST'])
def divide():
	divx = request.form.get('divx', type=int)
	divy = request.form.get('divy', type=int)
	try:
		result = divx / divy
	except:
		result = "Input Error"
	finally:
		return jsonify({'result' : result})