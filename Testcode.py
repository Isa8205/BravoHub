# from flask import Flask, request, render_template
# import pymysql
# from PIL import Image

# app = Flask(__name__)

# def is_square_image(file):
#     img = Image.open(file)
#     width, height = img.size
#     return width == height

# @app.route('/', methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         full_name = request.form['fullname']
#         username = request.form['username']
#         email = request.form['email']
#         password1 = request.form['password1']
#         password2 = request.form['password2']
#         profile = request.files['profile']

#         # Input validation
#         if len(password1) != 8:
#             return render_template('signup.html', errorpass="Passwords must be 8 characters long")
#         elif password1 != password2:
#             return render_template('signup.html', errorpass="Passwords must match")
#         elif not profile.filename:
#             return render_template('signup.html', errorpass="Profile picture is required")
#         elif not is_square_image(profile):
#             return render_template('signup.html', errorpass="Profile picture must be square")
#         else:
#             try:
#                 # Establishing a connection with the database
#                 connection = pymysql.connect(
#                     host='localhost', user='root', password='', database="BravoHub"
#                 )
#                 cursor = connection.cursor()

#                 # Insert user data into the database
#                 sql = '''INSERT INTO `users`(`Full_name`, `Username`, `email`, `profile`) 
#                          VALUES (%s, %s, %s, %s)'''
#                 cursor.execute(sql, (full_name, username, email, profile.filename))
#                 connection.commit()

#                 # Save profile picture
#                 profile.save('static/profiles')
#                 connection.close()

#                 return render_template('signup.html', message="Signup successful. Proceed to login.")
#             except Exception as e:
#                 print("Exception:", str(e))
#                 return render_template('signup.html', message="Signup failed. Please check your details and try again.")

#     else:
#         return render_template('signup.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template
# import pymysql
# from PIL import Image

# app = Flask(__name__)

# def is_square_image(file):
#     img = Image.open(file)
#     width, height = img.size
#     return width == height

# @app.route('/', methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         full_name = request.form['fullname']
#         username = request.form['username']
#         email = request.form['email']
#         password1 = request.form['password1']
#         password2 = request.form['password2']
#         profile = request.files['profile']

#         # Input validation
#         if len(password1) != 8:
#             return render_template('signup.html', errorpass="Passwords must be 8 characters long")
#         elif password1 != password2:
#             return render_template('signup.html', errorpass="Passwords must match")
#         elif not profile.filename:
#             return render_template('signup.html', errorpass="Profile picture is required")
#         elif not is_square_image(profile):
#             return render_template('signup.html', errorpass="Profile picture must be square")
#         else:
#             try:
#                 # Establishing a connection with the database
#                 connection = pymysql.connect(
#                     host='localhost', user='root', password='', database="BravoHub"
#                 )
#                 cursor = connection.cursor()

#                 # Insert user data into the database
#                 sql = '''INSERT INTO `users`(`Full_name`, `Username`, `email`, `profile`) 
#                          VALUES (%s, %s, %s, %s)'''
#                 cursor.execute(sql, (full_name, username, email, profile.filename))
#                 connection.commit()  # Commit the transaction

#                 # Save profile picture
#                 profile.save('static/profiles')
#                 connection.close()

#                 return render_template('signup.html', message="Signup successful. Proceed to login.")
#             except Exception as e:
#                 print("Exception:", str(e))
#                 return render_template('signup.html', message="Signup failed. Please check your details and try again.")

#     else:
#         return render_template('signup.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, render_template
# import pymysql
# from PIL import Image

# app = Flask(__name__)

# def is_square_image(file):
#     img = Image.open(file)
#     width, height = img.size
#     return width == height

# @app.route('/', methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         full_name = request.form['full_name']
#         username = request.form['username']
#         email = request.form['email']
#         password1 = request.form['password1']
#         password2 = request.form['password2']
#         profile = request.files['profile']

#         # Input validation
#         if len(password1) != 8:
#             return render_template('signup.html', errorpass="Passwords must be 8 characters long")
#         elif password1 != password2:
#             return render_template('signup.html', errorpass="Passwords must match")
#         elif not profile.filename:
#             return render_template('signup.html', errorpass="Profile picture is required")
#         elif not is_square_image(profile):
#             return render_template('signup.html', errorimg="Profile picture must be square")
#         else:
#             try:
#                 # Establishing a connection with the database
#                 connection = pymysql.connect(
#                     host='localhost', user='root', password='', database="BravoHub"
#                 )
#                 cursor = connection.cursor()

#                 # Insert user data into the database
#                 sql = '''INSERT INTO `users`(`Full_name`, `Username`, `email`, `profile`) 
#                          VALUES (%s, %s, %s, %s)'''
#                 data = (full_name, username, email, profile.filename)
#                 print("SQL Query:", sql % data)  # Print SQL query before execution
#                 cursor.execute(sql, data)
#                 connection.commit()  # Commit the transaction

#                 # Save profile picture
#                 profile.save('static/profiles')
#                 connection.close()

#                 return render_template('signup.html', message="Signup successful. Proceed to login.")
#             except Exception as e:
#                 print("Exception:", str(e))  # Log exception for debugging
#                 return render_template('signup.html', message="Signup failed. Please check your details and try again.")

#     else:
#         return render_template('signup.html')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import *
import pymysql
from PIL import Image

app = Flask(__name__)

def is_square_image(file):
    img = Image.open(file)
    width, height = img.size
    return width == height

# @app.route('/signup', methods=['POST', 'GET'])
# def signup():
#     print("Signup function called")  # Debugging: Print statement to check if function is called
#     if request.method == 'POST':
#         full_name = request.form['full_name']
#         username = request.form['username']
#         email = request.form['email']
#         password1 = request.form['password1']
#         password2 = request.form['password2']
#         profile = request.files['profile']
#         print("Profile filename:", profile.filename)  # Debugging: Print uploaded profile picture filename

#         # Input validation
#         if len(password1) <= 8:
#             return render_template('signup.html', errorpass="Passwords must be 8 characters long")
#         elif password1 != password2:
#             return render_template('signup.html', errorpass="Passwords must match")
#         elif not profile.filename:
#             return render_template('signup.html', errorimg="Profile picture is required")
#         elif not is_square_image(profile):
#             return render_template('signup.html', errorimg="Profile picture must be square")
#         else:
#             try:
#                 # Establishing a connection with the database
#                 print("Connected to database")  # Debugging: Print statement to check database connection
#                 connection = pymysql.connect(
#                     host='localhost', user='root', password='', database="BravoHub"
#                 )
#                 cursor = connection.cursor()

#                 # Insert user data into the database
#                 sql = '''INSERT INTO `users`(`full_name`, `username`, `email`, `password`, `profile`) 
#                             VALUES (%s, %s, %s, %s, %s)'''
#                 data = (full_name, username, email, password1, profile.filename)
#                 print("SQL Query:", sql % data)  # Debugging: Print SQL query before execution
#                 cursor.execute(sql, data)
#                 connection.commit()  # Commit the transaction

#                 # Save profile picture
#                 profile.save('static/profiles' + profile.filename)
#                 print("Image has been saved")
#                 connection.close()

#                 return render_template('signup.html', message="Signup successful. Proceed to login.")
#             except Exception as e:
#                 print("Exception:", str(e))  # Log exception for debugging
#                 return render_template('signup.html', message="Signup failed. Please check your details and try again.")

#     else:
#         return render_template('signup.html')

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Establish a database connection
        connection = pymysql.connect(
            host='localhost', user='root', password='', database='BravoHub'
        )
        print("Connected to the database")

        try:
            with connection.cursor() as cursor:
                # Execute the SQL query to fetch username and profile
                sql = '''SELECT `username`, `profile` FROM `users` WHERE `username`=%s AND `password`=%s'''
                cursor.execute(sql, (username, password))
                user_data = cursor.fetchone()  # Fetch the first row
                print("SQL:", sql % (username, password))

                if user_data:  # If user exists
                    session['username'] = user_data[0]  # Store username in session
                    session['profile'] = user_data[1]   # Store profile in session
                    return redirect('/')
                else:
                    return render_template('login.html', error='Invalid Credentials')
        except Exception as e:
            print("Exception:", str(e))
            return render_template('login.html', error='An error occurred while logging in')

        finally:
            connection.close()
    else :
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
