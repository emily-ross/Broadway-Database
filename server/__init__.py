from flask import Flask, render_template
import sys
sys.path.append(/user/Desktop/Compsci/Mongo Project/mongodb-project/)
import mongo_ask_insert

app = Flask(__name__, template_folder='../website')

@app.route('/')
def serve_app():
	return render_template('mongo_query.html')

@app.route('/input', methods=['GET', 'POST'])
def serve_input():
	if request.method == 'POST':
		get_user_input()
	return render_template('mongo_input.html')
	
app.run(debug=True)