from PIL import Image
from flask import *
import pymysql
from functions import *

app = Flask(__name__)

def is_square_image(file):
    img = Image.open(file)
    width, height = img.size
    return width == height

@app.route('/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        profile = request.files['profile']

        # Input validation
        if len(password1) != 8:
            return render_template('signup.html', errorpass="Passwords must be 8 characters long")
        elif password1 != password2:
            return render_template('signup.html', errorpass="Passwords must match")
        elif not profile.filename:
            return render_template('signup.html', errorpass="Profile picture is required")
        elif not is_square_image(profile):
            return render_template('signup.html', errorpass="Profile picture must be square")
        else:
            try:
                # Establishing a connection with the database
                connection = pymysql.connect(
                    host='localhost', user='root', password='', database="BravoHub"
                )
                cursor = connection.cursor()

                # Insert user data into the database
                sql = '''INSERT INTO `users`(`Full_name`, `Username`, `email`, `profile`) 
                         VALUES (%s, %s, %s, %s)'''
                cursor.execute(sql, (full_name, username, email, profile.filename))
                connection.commit()  # Commit the transaction

                # Save profile picture
                profile.save('static/profiles')
                connection.close()

                return render_template('signup.html', message="Signup successful. Proceed to login.")
            except Exception as e:
                print("Exception:", str(e))
                return render_template('signup.html', message="Signup failed. Please check your details and try again.")

    else:
        return render_template('signup.html')
  
@app.route('/login')
def login():
  return render_template('login.html')

if (__name__) == ("__main__"):
  app.run(debug=True)