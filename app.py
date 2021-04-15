from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=04fb8fc6ae8e62e2d9ba10c8a087985b')
    data = json.loads(req.content)
    return render_template('index.html', data=data)

@app.route('/visual')
def visual():
    return render_template('visuals.html')

if __name__ == "__main__":
    app.run(debug=True)

