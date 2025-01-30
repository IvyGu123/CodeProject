from flask import jsonify
from json import dumps
from flask import Flask, request
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
    mycursor.execute("SELECT * FROM book_info")
    myresult = mycursor.fetchall()
    books = []
    for x in myresult:
        books.append({'title': x[0],'price': x[1], 'status': x[2], 'id': x[4]})
    return dumps(books)

@app.route('/bookinfo/<int:book_id>')
def getBookById(book_id):
    mycursor.execute('SELECT * FROM book_info WHERE id =' +str(book_id))
    myresult = mycursor.fetchall()
    books = []
    for x in myresult:
        books.append({'title': x[0],'price': x[1], 'status': x[2], 'id': x[4]})
    return dumps(books)

@app.route('/bookinfo/addBook', methods=['POST'])
def addBook():
    new_book = {
        'title': 'Hello',
        'price': 17.00,
        'status': 'Available',
        'id': 3
    }
    mycursor.execute(
        "INSERT INTO book_info (title, price, status, id) VALUES (%s, %s, %s, %s)",
        (new_book['title'], new_book['price'], new_book['status'], new_book['id'])
    )
    mydb.commit()
    new_book['id'] = mycursor.lastrowid
    return dumps(new_book)

@app.route('/bookinfo/<int:book_id>', methods=['PUT'])
def updateBook(book_id):
    updated_data = request.json
    mycursor.execute(
        "UPDATE book_info SET title = %s, price = %s, status = %s WHERE id = %s",
        (updated_data.get('title', 'Updated Book'), 
         updated_data.get('price', 99.99), 
         updated_data.get('status', 'Available'), 
         book_id)
    )
    mydb.commit()
    if mycursor.rowcount == 0:
        return 'Book not found', 404

@app.route('/deleteBook/<int:book_id>', methods=['DELETE'])
def deleteBook(book_id):
    mycursor.execute('DELETE FROM book_info WHERE id = '+str(book_id))
    mydb.commit()
    return jsonify({"message": "ok"}), 200

@app.route('/buyBook/<int:book_id>', methods=['PUT'])
def buyBook(book_id):
    mycursor.execute("UPDATE book_info SET status = 'Sold' WHERE id = %s", (book_id,))
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404
    return jsonify({"message": "ok"}), 200

@app.route('/cancelBook/<int:book_id>', methods=['PUT'])
def cancelBook(book_id):
    mycursor.execute("UPDATE book_info SET status = 'Available' WHERE id = %s", (book_id,))
    mydb.commit()
    if mycursor.rowcount == 0:
        return jsonify({"message": "Book not found"}), 404
    return jsonify({"message": "ok"}), 200


if __name__ == '__main__':
    app.debug = True
    app.run()