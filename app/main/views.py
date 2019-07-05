from flask import render_template,request,redirect,url_for,abort
from . import main
from app.request import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    #Getting rando

    title = 'Home'

    return render_template('index.html', title = title )