#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
    Home route
    '''
    return render_template('0-index.py')

if __name__ == "__main__":
    app.run(port=5001)
