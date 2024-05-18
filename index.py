from flask import *
import pymysql

app = Flask(__name__)

# Database configuration
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'quarkblog'

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

@app.route('/')
def index():
    return render_template('trials.html')

@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.json.get("username", '')
    if check_username_availability(username):
        return jsonify({"available": False})
    else:
        return jsonify({"available": True})

if __name__ == '__main__':
    app.run(debug=True)
