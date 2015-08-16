"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import filmsoc
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Load index page and pass app object
    return render_template('pages/index.html', path = '/', filmsoc=filmsoc, year=datetime.now().year)

@app.route('/<path:path>')
def page(path):
    # Load any unfiltered page by searching it's path, passing app object
    return render_template('pages/'+path+'.html', path=path , filmsoc=filmsoc, year=datetime.now().year)