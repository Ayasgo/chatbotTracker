from flask import Blueprint, render_template, request
from .models import Session, db
from datetime import datetime
import re

# commands : start\s+(\w+)    end 


# Create a Blueprint
main = Blueprint('main', __name__)
new_session = Session()


@main.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        command = request.form.get('command').lower()

        if re.fullmatch('start\s+(\w+)', command):
            session_name = re.search('start\s+(\w+)', command)

    context = {}
    return render_template('index.html', **context)

@main.route('/add_session')
def add_session():
    new_session = Session(name='Morning Session', debut=time(9, 0), fin=time(12, 0))
    db.session.add(new_session)
    db.session.commit()
    return "Session added!"

#users = Session.query.all()
