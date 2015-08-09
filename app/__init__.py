from flask import Flask

app = Flask(__name__, template_folder = '', instance_path='/etc/www-v4', instance_relative_config=True )
app.config.from_pyfile('config.py')
from app import views
