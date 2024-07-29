from flask import Flask, render_template
import os
import calc as c

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask pythonserver', 200, {'Content-Type': 'text/plain'}

@app.route('/health')
def health():
    return 'OK', 200, {'Content-Type': 'text/plain'}

@app.route('/calc/<int:number>')
def calc(number):
    result = c.square(number)
    return str(result), 200, {'Content-Type': 'text/plain'}

@app.route('/links')
def links():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.logger.info(f'Server running on port {port}')
    app.run(host='0.0.0.0', port=port)