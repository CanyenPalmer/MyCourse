from app import db

class Hole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tee_id = db.Column(db.Integer, db.ForeignKey('tee.id'))
    hole_number = db.Column(db.Integer)
    yardage = db.Column(db.Integer)
    par = db.Column(db.Integer)  # e.g., 3, 4, or 5
