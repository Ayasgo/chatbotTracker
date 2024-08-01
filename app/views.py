from flask import Blueprint, render_template, request
from .models import Session, db
from datetime import datetime
import re

# commands : start\s+(\w+)    end  show


# Create a Blueprint
main = Blueprint('main', __name__)
session = None


@main.route('/', methods = ['GET', 'POST'])
def index():            

    context = {}
    return render_template('index.html', **context)

@main.route('/get_command', methods = ['POST'])
def get_command():
    global session

    if request.method == "POST":
        command = request.form.get('command').lower().strip()
        message = ''

        if re.fullmatch(r'start\s+(\w+)', command):
            if session:
                message = 'You must first end the current session'

            else :
                session_name = re.findall(r'start\s+(\w+)', command)[0]
                start_date = datetime.now().date()
                start_time = datetime.now().time()
                session = Session( name = session_name, 
                                   start_date =start_date,
                                   start_time = start_time)
                message = f'The "{session_name}" session was started successfully !'

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

#users = Session.query.all()
