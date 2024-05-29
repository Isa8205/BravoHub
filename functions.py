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