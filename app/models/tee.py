from app import db

class Tee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    tee_name = db.Column(db.String(50))
    total_yardage = db.Column(db.Integer)
    holes = db.relationship('Hole', backref='tee', lazy=True)
