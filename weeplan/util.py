from functools import wraps

from flask import redirect, render_template, session, url_for


def login_required(f):
    """
    Decorator for routes to require user be logged in
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('login'))

    return decorated_function
