from app import create_app, db
from app.models import Session
from datetime import timedelta

app = create_app()

def get_statistics(session_name):
    sessions = db.session.query(Session).filter_by(name='coding')

    time = timedelta()
    for s in sessions:
        time+= s.get_time()

    return time

def get_sessions_names():
    return [ s.name for s in db.session.query(Session).group_by('name') ]

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()
    print(get_statistics('coding'))
    print(get_sessions_names())

if __name__ == "__main__":
    pass
    #app.run(debug=True)
