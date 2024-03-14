from flask import Flask, render_template , url_for
from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, DateTimeField
from datetime import datetime
from wtforms.validators import DataRequired , Email

app = Flask(__name__)


book = [
    {"title": "Book 1", "author": "Author 1", "genre": "Fiction", "isbn": "123456"},
    {"title": "Book 2", "author": "Author 2", "genre": "Non-Fiction", "isbn": "789012"},
    
]

member = [
    {"name": "John Doe", "email": "john@example.com", "membership_id": "001", "address": "123 Main St"},
    {"name": "Jane Smith", "email": "jane@example.com", "membership_id": "002", "address": "456 Elm St"},
    
]

transactions = [
    {"book_title": "Book 1", "member_name": "John Doe", "date_borrowed": "2024-03-14", "date_returned": " "},
    
]


@app.route('/')
def index():
    return render_template('library_management_system.html', books=book, members=member, transactions=transactions)

@app.route('/books',methods=['GET','POST'])
def books():
    return render_template('book.html')

@app.route('/members',methods=['GET','POST'])
def members():
    return render_template('member.html')


if __name__ == '__main__':
    app.run(debug=True)
