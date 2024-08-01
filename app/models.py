from . import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    start = db.Column(db.Time)
    end = db.Column(db.Time)

    def __repr__(self):
        return f'<User {self.username}>'
