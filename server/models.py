from email.policy import default
from flask_login import UserMixin
from server import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(20), nullable = False)
    lname = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(40), unique = True, nullable = False)
    city = db.Column(db.String(20), nullable = False)
    image_file = db.Column(db.String(50), default = 'default.png', nullable = False)
    zip_code = db.Column(db.Integer,nullable = False)
    password = db.Column(db.String(30), nullable = False)

    def __repr__(self) -> str:
        return f"User({self.id}, {self.fname}, {self.lname}, {self.email}, {self.city}, {self.zip_code})"