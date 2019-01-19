from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "This is a fuckall base of an API"


@app.route('/episteme', methods=['GET','POST'])
def analyze():

    l = ['Dog','Poo','Shampoo']
    response = {'result': random.choice(l)}
    response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(response)

if __name__ == ('__main__'):
    app.run()
