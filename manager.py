from flask import Flask
from flask_bootstrap import  Bootstrap
from flask_wtf import CSRFProtect
from flaskpractice01 import practice01

print(__name__)
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'ldhuping'
crsf = CSRFProtect(app)

if __name__ == 'manager':
    app.register_blueprint(practice01, url_prefix='/practice01')
    app.run(debug=True)