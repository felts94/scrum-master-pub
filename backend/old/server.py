from flask import Flask, session, redirect, url_for, escape, request, render_template, jsonify
import os, datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message':'Hello, World!', 'time':str(datetime.datetime.now())})


app.run(host='0.0.0.0', debug=True)