from app import db

class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
