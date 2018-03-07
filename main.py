from flask import Flask, jsonify, request
import math

app = Flask(__name__)

name = "Katie Carroll"

@app.route("/name", methods= ['GET'])
def json_name():
    data = {
        "name": name
    }

    return jsonify(data)

@app.route("/hello/name", methods= ['GET'])
def hello_name():
    data = {
        "message": "hello you good looking human, {}".format(name)
    }

    return jsonify(data)

@app.route("/distance", methods= ['POST'])
def find_distance():
    a = [2,4]
    b = [5,6]

    d1 = (a[0] - b[0]) **2
    d2 = (a[1] - b[1]) **2

    d = math.sqrt(d1+d2)

    data = {
        "distance": d,
        "a" : a,
        "b" : b,
    }

    return jsonify(data)
