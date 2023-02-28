#!/usr/bin/env python3
'''
Basic flask application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    '''
    Home route
    '''
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()