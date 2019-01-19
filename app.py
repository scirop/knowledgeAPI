from flask import Flask, jsonify
import random

app = Flask(__name__)

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
