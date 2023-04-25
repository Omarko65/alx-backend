#!/usr/bin/env python3
'''flask application'''
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    '''Config class for Babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = LANGUAGE[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    ''' route home '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
