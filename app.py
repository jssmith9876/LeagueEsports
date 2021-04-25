from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index_serve():
    return render_template("index.html")

@app.route('/test.json')
def get_data():
    with open('static/data/test.json', 'r') as json_file:
        data = json.load(json_file)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)