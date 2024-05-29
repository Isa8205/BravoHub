import os
import sqlite3
from functools import wraps
from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from functions import *

app = Flask(__name__)
app.secret_key = "fjsd8sf8s9fdsaHh"

# Database configuration
db_path = 'bravohub.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    profile = db.Column(db.String(100))
    articles = db.relationship('Article', backref='user', lazy=True)

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('users.username'), nullable=False)
    genre = db.Column(db.String(50))
    headline = db.Column(db.String(255))
    context = db.Column(db.Text)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('users.username'), nullable=False)
    subject = db.Column(db.String(255))
    description = db.Column(db.Text)


# The functions to be used within the application
def check_username_availability(username):
    user = User.query.filter_by(username=username).first()
    return user is not None

def create_database():
    if not os.path.exists(db_path):
        db.create_all()
        print("Database created successfully")

# The routes to the application
@app.route('/admin')
def admin():
    sql = text('''SELECT username, full_name, password, profile FROM users''')

    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()

        return render_template('admin.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('admin.html', page_data=[])
    finally:
        conn.close()

@app.route('/')
def homepage():
    sql = text('''
            SELECT a.username, a.headline, a.context, u.profile, a.date
            FROM articles a
            JOIN users u ON a.username = u.username
        ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()


@app.route('/technology')
def technology():
    sql = text('''
        SELECT a.username, a.headline, a.context, u.profile, a.date
        FROM articles a
        JOIN users u ON a.username = u.username
        WHERE a.genre = "Technology"
    ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()

@app.route('/sports')
def sports():
    sql = text('''
        SELECT a.username, a.headline, a.context, u.profile, a.date
        FROM articles a
        JOIN users u ON a.username = u.username
        WHERE a.genre = "Sports"
    ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()

@app.route('/fashion')
def fashion():
    sql = text('''
        SELECT a.username, a.headline, a.context, u.profile, a.date
        FROM articles a
        JOIN users u ON a.username = u.username
        WHERE a.genre = "Fashion"
    ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()

@app.route('/politics')
def politics():
    sql = text('''
        SELECT a.username, a.headline, a.context, u.profile, a.date
        FROM articles a
        JOIN users u ON a.username = u.username
        WHERE a.genre = "Politics"
    ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()

@app.route('/other')
def other():
    sql = text('''
        SELECT a.username, a.headline, a.context, u.profile, a.date
        FROM articles a
        JOIN users u ON a.username = u.username
        WHERE a.genre = "other"
    ''')
    try:
        conn = db.engine.connect()
        result = conn.execute(sql)
        page_data = result.fetchall()
        
        return render_template('index.html', page_data=page_data)
    except Exception as e:
        print(f"Exception: {e}")
        return render_template('index.html', page_data=[])
    finally:
        conn.close()

@app.route('/review', methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        username = session['username']
        subject = request.form['subject']
        description = request.form['description']
        
        try:
            review = Review(username=username, subject=subject, description=description)
            db.session.add(review)
            db.session.commit()
            return '<p>We have received your message and are working on it</p> <a href="/">Back home</a>'
        except Exception as e:
            print("Exception: ", str(e))
            return '<p>We encountered an error, please try again<a href="/">Back home</a></p>'
            
    else:
        return '<p>We encountered an error please try again</p> <a href="/">Back home</a>'

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        profile = request.files['profile']
        
        if profile:
            profile_name = profile.filename
            profile.save('static/profiles/' + profile_name)
        else:
            profile_name = 'avatar6.png'

        # Input validation
        if len(password1) < 8:
            return render_template('signup.html', errorpass="Passwords must be at least 8 characters long")
        elif password1 != password2:
            return render_template('signup.html', errorpass="Passwords must match")
        else:
            try:
                user = User(full_name=full_name, username=username, email=email, password=password1, profile=profile_name)
                db.session.add(user)
                db.session.commit()
                return render_template('signup.html', message="Signup successful. Proceed to login.")
            except Exception as e:
                print("Exception:", str(e))
                return render_template('signup.html', error="Signup failed. Please check your details and try again.")

    else:
        return render_template('signup.html')
    
@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.json.get("username", '')
    if check_username_availability(username):
        return jsonify({"available": False})
    else:
        return jsonify({"available": True})
  
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                session['username'] = user.username
                session['profile'] = user.profile
                session['full_name'] = user.full_name
                return redirect('/')
            else:
                return render_template('login.html', error='Invalid Credentials')
        except Exception as e:
            print("Exception:", str(e))
            return render_template('login.html', error='An error occurred while logging in please try again')

    else:
        return render_template('login.html')
    

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/upload', methods=['POST', 'GET'])
@login_required
def upload():
    if request.method == 'POST':
        username = session.get('username')
        genre = request.form['genre']
        headline = request.form['headline']
        context = request.form['context']
        
        try:
            article = Article(username=username, genre=genre, headline=headline, context=context)
            db.session.add(article)
            db.session.commit()
            return render_template('upload.html', success="Upload successful")
        except Exception as e:
            print("Exception: ", str(e))
            return render_template('upload.html', errorupload="Failed to upload please try again")
            
    else:
        return render_template('upload.html')

        
    
@app.route('/account')
def account():
    username = session['username']
    page_data = db.session.query(Article, User).join(User, Article.username == User.username).filter(User.username == username).all()
    return render_template('account.html', page_data=page_data)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    with app.app_context():
        create_database()
    app.run(debug=True)
