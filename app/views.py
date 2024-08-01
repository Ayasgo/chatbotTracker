from flask import Blueprint, render_template
from .models import User

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    context = {}
    return render_template('index.html', **context)

@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
