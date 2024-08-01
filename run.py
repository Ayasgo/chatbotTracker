from app import create_app, db
from app.models import Session
from datetime import timedelta, datetime

app = create_app()

def get_session_statistics(db, session_name):
    sessions = db.session.query(Session).filter_by(name= session_name)
    time = timedelta()
    for s in sessions:
        time+= s.get_time()

    return time

def get_today_statistics(db):
    today=datetime.now().date()
    sessions = db.session.query(Session).filter_by(start_date = today)
    d = {}
    for s in sessions:
        time = d.get(s.name, timedelta()) + s.get_time()
        d[s.name] = time
    return { k: str(v)[: str(v).rfind('.')] for k,v in d.items()}

def get_all_statistics(db):
    sessions_names = get_sessions_names(db)
    d = {}
    for sn in sessions_names:
        time = str(get_session_statistics(db, sn))
        d[sn] = time[ :time.rfind('.')]
    return d

def get_sessions_names(db):
    return [ s.name for s in db.session.query(Session).group_by('name') ]

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()
    print(get_session_statistics(db, 'coding'))
    print(get_sessions_names(db))
    print(get_all_statistics(db))
    print(get_today_statistics(db))

if __name__ == "__main__":
    pass
    #app.run(debug=True)
