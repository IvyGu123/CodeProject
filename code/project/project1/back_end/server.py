from json import dumps
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import mysql.connector
mydb = mysql.connector.connect (
    host="localhost",
    user="root",    
    password="LiterallyIvy123",
    database="book"
)
print (mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM book_info")
myresult = mycursor.fetchall()
books = []
for x in myresult:
    books.append({'title': x[0],'price': x[1], 'status': x[2], 'id': x[4]})
    
print(books)

@app.route('/')
def hello():
    return 'HELLO WORLD!'

@app.route('/bookinfo')
def getBookInfo():
    return dumps(books)

@app.route('/bookinfo/<int:book_id>')
def getBookById(book_id):
    for book in books:
        if book['id'] == book_id:
            return dumps(book)
    return 'Book not found', 404    

@app.route('/bookinfo', methods=['POST'])
def addBook():
    new_book = {
        'id': len(books) + 1,
        'title': 'New Book',
        'price': 0,
        'status': 'Available'
    }
    books.append(new_book)
    return dumps(new_book)

@app.route('/bookinfo/<int:book_id>', methods=['PUT'])
def updateBook(book_id):
    for book in books:
        if book['id'] == book_id:
            book['title'] == 'Updated Book'
            book['price'] == 99.99
            book['status'] == 'Available'
            return dumps(book)
    return 'Book not found', 404

@app.route('/deleteBook/<int:book_id>', methods=['DELETE'])
def deleteBook(book_id):
    cursor.execute('DELETE * FROM books WHERE id = '+str(book_id))

@app.route('/buyBook/<int:book_id>', methods=['PUT'])
def buyBook(book_id):
    for book in books:
        if book['id'] == book_id:
            print(book['status'])
            book['status'] = 'Sold'
            return dumps(book)
    return 'Book not found', 404

@app.route('/cancelBook/<int:book_id>', methods=['PUT'])
def cancelBook(book_id):
    for book in books:
        if book['id'] == book_id:
            book['status'] = 'Available'
            return dumps(book)
    return 'Book not found', 404

if __name__ == '__main__':
    app.debug = True
    app.run()