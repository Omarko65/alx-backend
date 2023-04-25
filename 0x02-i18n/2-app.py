#!/usr/bin/env python3
'''flask application'''
from flask import Flask, render_template
from flask_babel import Babel

def get_locale():
    ''' get_locale '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])

class Config():
    '''Config class for Babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_LOCALE_SELECTOR = get_locale


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

@app.route("/")
def index():
    ''' route home '''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
