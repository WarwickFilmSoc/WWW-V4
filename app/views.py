"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, session, request
from flask_sso import SSO
import filmsoc
from app import app

app.jinja_env.globals['filmsoc'] = filmsoc
app.jinja_env.globals['app'] = app
app.jinja_env.globals['year'] = year=datetime.now().year

# Create SSO instance
sso = SSO(app=app)

# Handles the login information from Shibboleth
@sso.login_handler
def login(user_info):
    session['user'] = user_info
       
    # return url specified in query string
    return_url = request.args.get('return')

    if return_url:
        return redirect(return_url)
    else:
        # If not specified send to home
        return redirect('/')

@app.route('/logout')
def logout():
    try:
        session.pop('user')
    except:
        pass
    return redirect('/Shibboleth.sso/Logout?return=/')

@app.route('/')
@app.route('/index')
def index():
    # Load index page and pass app object
    return render_template('pages/index.html', path = '/')

@app.route('/<path:path>')
def page(path):
    # Load any unfiltered page by searching it's path, passing app object
    return render_template('pages/'+path+'.html', path=path)