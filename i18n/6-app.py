#!/usr/bin/env python3
"""Babel module"""
from flask import Flask, request, render_template, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def hello_world():
    """home route"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Function that determines the best locale based on priorities."""
    locale = request.args.get('locale')  # 1. Locale from URL parameters
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') and g.user['locale'] in app.config['LANGUAGES']:  # 2. Locale from user settings
        return g.user['locale']

    locale = request.headers.get('locale')  # 3. Locale from request header
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])  # 4. Default locale


def get_user():
    """Function that returns a user dictionary."""
    id = request.args.get('login_as')
    if id:
        return users[int(id)]
    else:
        return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user."""
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
