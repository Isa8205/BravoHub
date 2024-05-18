from flask import *
import pymysql

app = Flask(__name__)
app.secret_key = "fjsd8sf8s9fdsaHh"

# Database configuration
db_host = "localhost"
db_user = "root"
db_password = ''
db_name = "quarkblog"

# The functions to be used within the application
def check_username_availability(username):
    try:
        # Connect to MySQL database
        connection = pymysql.connect(host=db_host,
                                     user=db_user,
                                     password=db_password,
                                     database=db_name,
                                     cursorclass=pymysql.cursors.DictCursor)
        print('connected to the database')

        # Check if the username exists in the database
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            
        if result:
            return True
        else:
            return False

    except Exception as e:
        print("Error:", e)
        return False
    
    finally:
        connection.close()
#End of the fuctions

 
# The routes to the application
@app.route('/')
def homepage():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username'''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/technology')
def technology():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE a.genre = "Technology" '''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/sports')
def sports():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE a.genre = "Sports" '''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/fashion')
def fashion():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE a.genre = "Fashion" '''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/politics')
def business():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE a.genre = "Politics" '''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/other')
def other():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE a.genre = "Other" '''
    cursor.execute(sql)
    page_data = cursor.fetchall()
    
    connection.close()
    return render_template('index.html',  page_data=page_data)

@app.route('/review', methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        username = session['username']
        subject = request.form['subject']
        description = request.form['description']
        
        connection = pymysql.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        cursor = connection.cursor()
        
        sql ='''INSERT INTO `reviews`(`username`, `subject`, `description`) VALUES (%s, %s, %s)'''
        
        try:
            cursor.execute(sql, (username, subject, description))
            print("Query: ", sql % (username, subject, description))
            connection.commit()
            print("changes made to the database")
            return '<p>We have received your message and are working on it</p> <a href="/">Back home</a>'
        except Exception as e:
            print("Exception: ", str(e))
            return '<p>We encountered an error, please try again<a href="/">Back home</a></p>'
            
        finally:
            connection.close()
            
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
            profile_pic = profile
            profile_name = profile.filename
            # Save profile picture
            profile_pic.save('static/profiles/' + profile_name)
        else:
            profile_name = 'avatar6.png'

        # Input validation
        if len(password1) < 8:
            return render_template('signup.html', errorpass="Passwords must be at least 8 characters long")
        elif password1 != password2:
            return render_template('signup.html', errorpass="Passwords must match")
        else:
            try:
                # Establishing a connection with the database
                connection = pymysql.connect(
                    host=db_host, user=db_user, password=db_password, database="quarkblog"
                )
                print("Conneccted to the database")
                cursor = connection.cursor()

                # Insert user data into the database
                data = (full_name, username, email, password1, profile_name)
                sql = '''INSERT INTO `users`(`full_name`, `username`, `email`, `password`, `profile`) 
                         VALUES (%s, %s, %s, %s, %s)'''
                cursor.execute(sql, data)
                
                connection.commit()  # Commit the transaction

                return render_template('signup.html', message="Signup successful. Proceed to login.")
            except Exception as e:
                print("Exception:", str(e))
                return render_template('signup.html', error="Signup failed. Please check your details and try again.")
            finally:
                connection.close()

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

        # Establish a database connection
        connection = pymysql.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )

        try:
            with connection.cursor() as cursor:
                # Execute the SQL query to fetch username and profile
                sql = '''SELECT `full_name`, `username`, `password`, `profile` FROM `users` WHERE `username`=%s AND `password`=%s'''
                cursor.execute(sql, (username, password))
                user_data = cursor.fetchone()  # Fetch the first row
                # print(user_data)

                if user_data:  # If user exists
                    session['username'] = user_data[1]  # Store username in session
                    session['profile'] = user_data[3]   # Store profile in session
                    session['full_name'] = user_data[0]
                    return redirect('/')
                else:
                    return render_template('login.html', error='Invalid Credentials')
        except Exception as e:
            print("Exception:", str(e))
            return render_template('login.html', error='An error occurred while logging in please try again')

        finally:
            connection.close()
    else :
        return render_template('login.html')
    
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        username = session['username']
        genre = request.form['genre']
        headline = request.form['headline']
        context = request.form['context']
        
        connection = pymysql.connect(
            host=db_host, user=db_user, password=db_password, database=db_name
        )
        cursor = connection.cursor()
        
        sql = '''INSERT INTO `articles`(`username`, `genre`, `headline`, `context`) VALUES (%s, %s, %s, %s)'''
        
        try:
            cursor.execute(sql, (username, genre, headline, context))
            connection.commit()
            return render_template('upload.html', success="Upload successful")
        except Exception as e:
            print("Exception: ", str(e))
            return render_template('upload.html', errorupload="Failed to upload please try again")
        finally:
            connection.close()
            
    else:
        return render_template('upload.html')
        
    
@app.route('/account')
def account():
    connection = pymysql.connect(
        host=db_host, user=db_user, password=db_password, database=db_name
    )
    cursor = connection.cursor()
    username = session['username']
    
    # The sql query itself
    sql = '''SELECT a.username, a.context, a.headline, a.date, u.profile FROM articles a JOIN users u ON a.username = u.username WHERE u.username = %s '''
    cursor.execute(sql, (username))
    page_data = cursor.fetchall()
    print(page_data)
    
    connection.close()
    return render_template('account.html',  page_data=page_data)
    
@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')


if (__name__) == ("__main__"):
  app.run(debug=True)