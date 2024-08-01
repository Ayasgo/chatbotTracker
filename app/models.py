from . import db

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    debut = db.Column(db.Time)
    fin = db.Column(db.Time)

    def __repr__(self):
        return f'<User {self.username}>'
