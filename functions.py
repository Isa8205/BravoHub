def check_username_availability(username):
    user = User.query.filter_by(username=username).first()
    return user is not None

def create_database():
    if not os.path.exists(db_path):
        db.create_all()
        print("Database created successfully")