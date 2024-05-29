from app import db
from datetime import datetime

# The database model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)
    genre = db.Column(db.String(80), nullable = False)
    headline = db.Column(db.String(80), nullable = False)
    context = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default = lambda:datetime.utcnow)

    def __repr__(self):
        return f'<Article {self.headline}>'
    
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)
    subject = db.Column(db.String(80), nullable = False)
    description = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f'<Review {self.subject}>'
    
# import sqlite3

# # Connect to the database (or create it if it doesn't exist)
# conn = sqlite3.connect('bravohub.db')

# # Create a cursor object
# cursor = conn.cursor()

# # Execute a query
# cursor.execute('SELECT * FROM reviews')

# # Fetch and print the results
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Close the connection
# conn.close()

    