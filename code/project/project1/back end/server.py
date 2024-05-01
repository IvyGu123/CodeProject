from json import dumps
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'HELLO WORLD!'

@app.route('/bookinfo')
def getBookInfo():
    book = {
        'title': 'The Great Gatsby',
        'price': 12.99
    }
    return dumps(book)

if __name__ == '__main__':
    app.debug = True
    app.run()