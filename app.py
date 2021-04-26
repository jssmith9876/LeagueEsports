from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Default page => index.html
@app.route('/')
@app.route('/index.html')
def index_serve():
    return render_template("index.html")

# Teams page
@app.route('/teams.html')
def teams_serve():
    return render_template("teams.html")

# Log in page
@app.route('/log_in.html')
def login_serve():
    return render_template("log_in.html")

# sign up page
@app.route('/sign_up.html')
def signup_serve():
    return render_template("sign_up.html")

# When the app needs to load json => send the data 
@app.route('/test.json')
def get_data():
    with open('static/data/test.json', 'r') as json_file:
        data = json.load(json_file)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)