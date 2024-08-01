from flask import Blueprint, render_template, request
from .models import Session, db
from datetime import datetime
import re

# commands : start\s+(\w+)    end 


# Create a Blueprint
main = Blueprint('main', __name__)
session = None


@main.route('/', methods = ['GET', 'POST'])
def index():            

    context = {}
    return render_template('index.html', **context)

@main.route('/get_command', methods = ['POST'])
def get_command():
    if request.method == "POST":
        command = request.form.get('command').lower().strip()
        message = ''

        if re.fullmatch(r'start\s+(\w+)', command):
            if session:
                message = 'You must first end the current session'
            else :
                session_name = re.findall(r'start\s+(\w+)', command)[0]
                start = datetime.now()
                session = Session( name = session_name, start = start)
                message = f' The {session_name} session was started successfully !'

        elif command == 'end':
            end = datetime.now()
            session.end = end
            db.session.add(session)
            db.session.commit()

            message = f' The {session.name} session was ended successfully !'
            session = None
        
        else:
            message = "Invalid command"

        return message

#users = Session.query.all()
