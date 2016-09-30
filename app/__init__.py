from flask import Flask

app = Flask(__name__, template_folder = '', instance_path='/usr/share/www-v4', instance_relative_config=True )
if('v4_web' in socket.gethostname()):
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.Config')

from app import views
