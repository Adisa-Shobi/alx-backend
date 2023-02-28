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
    return 'Hello, World!'
