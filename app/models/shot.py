from app import db

class Shot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    hole_id = db.Column(db.Integer)
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    club = db.Column(db.String(50))
    start_x = db.Column(db.Float)
    start_y = db.Column(db.Float)
    end_x = db.Column(db.Float)
    end_y = db.Column(db.Float)
    lie = db.Column(db.String(50))
    strokes_taken = db.Column(db.Float)
    target_line = db.Column(db.String(100))

    # Performance input fields
    fairway_hit = db.Column(db.String(10))  # left, right, long, short, yes
    gir = db.Column(db.String(10))          # left, right, long, short, yes
    chips = db.Column(db.Integer)
    putts = db.Column(db.Integer)
    hazards = db.Column(db.Integer)
    penalties = db.Column(db.Integer)
