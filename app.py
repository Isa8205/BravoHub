from flask import *
import pymysql

app = Flask(__name__)

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
        if len(password1) <= 8:
            return render_template('signup.html', errorpass="Passwords must be 8 characters long")
        elif password1 != password2:
            return render_template('signup.html', errorpass="Passwords must match")
        else:
            try:
                # Establishing a connection with the database
                connection = pymysql.connect(
                    host='localhost', user='root', password='', database="BravoHub"
                )
                print("Conneccted to the database")
                cursor = connection.cursor()

                # Insert user data into the database
                data = (full_name, username, email, password1, profile.filename)
                sql = '''INSERT INTO `users`(`full_name`, `username`, `email`, `password`, `profile`) 
                         VALUES (%s, %s, %s, %s, %s)'''
                cursor.execute(sql, data)
                
                connection.commit()  # Commit the transaction
                print("The changes have been made to the database")

                # Save profile picture
                profile.save('static/profiles' + profile.filename)
                
                connection.close()

                return render_template('signup.html', message="Signup successful. Proceed to login.")
            except Exception as e:
                print("Exception:", str(e))
                return render_template('signup.html', message="Signup failed. Please check your details and try again.")

    else:
        return render_template('signup.html')
  
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        connection=pymysql.connect(
            host='localhost', user='root', password='',database='BravoHub'
            )
        data = (username,password)
        sql='''SELECT `username`, `password` FROM `users` WHERE `username`=%s AND `password`=%s'''
        cursor=connection.cursor()
        cursor.execute(sql, data)
        print("SQL Query:", sql % data)
        if cursor.rowcount == 0:
            return render_template('login.html', error='Invalid Credentials')
        else:
            session['key']=username
            return redirect('/')
    else:
        return render_template('login.html')

if (__name__) == ("__main__"):
  app.run(debug=True)