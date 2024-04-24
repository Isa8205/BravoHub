# def validate_image_size(image_file, max_width=None, max_height=None):
#   """
#   Validates the size of an uploaded image.

#   Args:
#     image_file: The uploaded image file object.
#     max_width: The maximum allowed width of the image.
#     max_height: The maximum allowed height of the image.

#   Returns:
#     True if the image size is valid, False otherwise.
#   """

#   if image_file:
#     image = Image.open(image_file)
#     width, height = image.size

#     if max_width and width > max_width:
#       return render_template('signup.html', errorimg="Ensure the image is ")

#     if max_height and height > max_height:
#       return False
    
#     if width == height:
#       return "square"
#     else:
#       return "N-square"

#   # else:
#   #   # print(f"Error validating image size: {e}")
#   #   return False
# def confirm_image_dimensions(imagefile):
#   sqrimage = validate_image_size(profile)
#   if sqrimage == "square":
#     profile.save('static/profiles' + profile.filename)      
#   else:
#     return render_template('signup.html', errorimg = "Ensure the image is a square")
  
from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        full_name = request.form['fullname']
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
        elif profile.filename == '':
            return render_template('signup.html', errorpass="Profile picture is required")
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
                connection.commit()

                # Save profile picture
                profile.save('<path_to_save_profile_picture>')
                connection.close()

                return render_template('signup.html', message="Signup successful. Proceed to login.")
            except Exception as e:
                print("Exception:", str(e))
                return render_template('signup.html', message="Signup failed. Please check your details and try again.")

    else:
        return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
