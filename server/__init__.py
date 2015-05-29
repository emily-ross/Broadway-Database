from flask import Flask, render_template, request
import sys
sys.path.append("/Users/emiross/Desktop/Compsci/Mongo Project/mongodb-project/")
import mongo_ask_insert

app = Flask(__name__, template_folder='../website')

@app.route('/')
def serve_app():
	return render_template('mongo_query.html')

@app.route('/input', methods=['GET', 'POST'])
def serve_input():
	show = None
	if request.method == 'POST':
		show = mongo_ask_insert.get_user_input(request)
	return render_template('mongo_input.html', show=show)
	
app.run(debug=True)