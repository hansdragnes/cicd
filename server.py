from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask pythonserver', 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f'Server running on port {port}')
    app.run(host='0.0.0.0', port=port)