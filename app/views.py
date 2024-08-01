from flask import Blueprint, render_template, request
from .models import Session, db
from .statistics import *
from datetime import datetime
import re

# commands : start\s+((\w|_)+)  -  end  - stat\s(\w+)


# Create a Blueprint
main = Blueprint('main', __name__)
session = None

def get_message(command):
    message = ''

    if re.fullmatch(r'start\s+((\w|_)+)', command):
        if session:
            message = 'You must first end the current session'

        else :
            session_name = re.findall(r'start\s+((\w|_)+)', command)[0]
            start_date = datetime.now().date()
            start_time = datetime.now().time()
            session = Session( name = session_name, 
                                start_date =start_date,
                                start_time = start_time)
            message = f'The "{session_name}" session was started successfully !'

    elif re.fullmatch(r'stat\s(\w+)', command):
        attribut = re.findall(r'stat\s(\w+)', command)[0]
        if attribut == 'all':
            stats = get_all_statistics(db)
            message = '<ul>'
            for n,s in stats.items():
                message += f'<li>{n} : {s}</li>'
            message += '</ul>'

        elif attribut == 'today':
            stats = get_today_statistics(db)
            message = '<ul>'
            for n,s in stats.items():
                message += f'<li>{n} : {s}</li>'
            message += '</ul>'

        else:
            message = get_session_statistics(db, attribut)

    elif command == 'end' and session:
        end_date = datetime.now().date()
        end_time = datetime.now().time()
        session.end_date = end_date
        session.end_time = end_time
        db.session.add(session)
        db.session.commit()

        message = f'The "{session.name}" session was ended successfully !'
        session = None

    else:
        message = "Invalid command"

    return message

@main.route('/', methods = ['GET', 'POST'])
def index():            

    context = {}
    return render_template('index.html', **context)

@main.route('/get_command', methods = ['POST'])
def get_command():
    global session

    if request.method == "POST":
        command = request.form.get('command').lower().strip()
        return get_message(command)

#users = Session.query.all()
