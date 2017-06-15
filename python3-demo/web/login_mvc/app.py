#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Perlou(perloukevin@gmail.com)'


'''
web application.
'''

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def sign_form():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'Perlou' and password == 'password':
        return render_template('success.html', username = username)

    return render_template('signin.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
