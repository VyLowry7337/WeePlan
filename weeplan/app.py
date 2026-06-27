import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from util import login_required
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure cookies
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'

# Init sessions
Session(app)

# Configure DB
db = SQL('sqlite:///dashboard.db')


@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/login')
def login():
    pass


@app.route('/dashboard')
def dashboard():
    pass


@app.route('/register')
def register():
    pass


@app.route('/planner')
def planner():
    pass


@app.route('/tasks')
def tasks():
    pass
