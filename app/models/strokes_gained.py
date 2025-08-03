from app import db

class StrokesGainedBaseline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Integer)
    lie_type = db.Column(db.String(50))
    strokes_to_hole_pga = db.Column(db.Float)
    strokes_to_hole_by_handicap = db.Column(db.JSON)
