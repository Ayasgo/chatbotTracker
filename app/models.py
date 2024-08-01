from . import db
from datetime import datetime

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    start_date = db.Column(db.Date)
    start_time = db.Column(db.Time)

    end_date = db.Column(db.Date)
    end_time = db.Column(db.Time)

    def get_time(self):
        if self.end_date and self.end_time:
            start = datetime.combine(self.start_date, self.start_time)
            end = datetime.combine(self.end_date, self.end_time)
            time = end - start
            return time
