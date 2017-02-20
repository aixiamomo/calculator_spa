# -*- coding: utf-8 -*-
import re
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/_calculate')
def calculate():
    number1 = request.args.get('number1', '0')
    operator = request.args.get('operator', '+')
    number2 = request.args.get('number2')
    m = re.match('-?\d+', number1)
    n = re.match('-?\d+', number2)
    if m is None or n is None or operator not in '+-*/':
        return jsonify(result='I Catch a BUG!')
    if operator == '/':
        result = eval(number1 + operator + str(float(number2)))
    else:
        result = eval(number1 + operator + number2)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
