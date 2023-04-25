#!/usr/bin/python3
'''flask application'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
'''app route to home'''
def home():
    return render_template('0-index.html')
