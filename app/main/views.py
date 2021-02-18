from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User
from . import main
from .. import db
from .forms import NameForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/projects')
def projects():
    return render_template('projects.html')

@main.route('/links')
def links():
    return render_template('links.html')

