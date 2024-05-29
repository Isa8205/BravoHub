from flask import *
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bravohub.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

    sql = '''SELECT * FROM `reviews`'''

    connection = db.engine.connect()
    print("connected to the database")

    try:
        result = connection.execute(text(sql))
        page_data = result.fetchall()
        if page_data:
            for row in page_data:
                print(row)
        else:
            print('No data found')
    except SQLAlchemyError as e:
        print(f"SQLAlchemy Exception: {e}")
    except Exception as e:
        print(f"General Exception: {e}")
    finally:
        connection.close()

    return render_template('trials.html', results=page_data)


@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.json.get("username", '')
    if check_username_availability(username):
        return jsonify({"available": False})
    else:
        return jsonify({"available": True})

if __name__ == '__main__':
    app.run(debug=True)
