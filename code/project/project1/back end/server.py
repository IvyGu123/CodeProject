from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'HELLO WORLD!'

@app.route('/price')
def price():
    return '150'

@app.route('/book')
def bookName():
    return 'book name'

if __name__ == '__main__':
    app.debug = True
    app.run()