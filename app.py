from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Default page => index.html
@app.route('/')
def index_serve():
    return render_template("index.html")

# When the app needs to load json => send the data 
@app.route('/test.json')
def get_data():
    with open('static/data/test.json', 'r') as json_file:
        data = json.load(json_file)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)