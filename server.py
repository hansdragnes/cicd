from flask import Flask, render_template, request
import os
import calc as c

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask pythonserver', 200, {'Content-Type': 'text/plain'}


@app.route('/calc/<int:number>')
def calc(number):
    result = c.square(number)
    return str(result), 200, {'Content-Type': 'text/plain'}

@app.route('/links')
def links():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calc.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    result = c.add(number1, number2)  # Assuming you have an add function in calc module
    return f'The result is {result}', 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.logger.info(f'Server running on port {port}')
    app.run(host='0.0.0.0', port=port)