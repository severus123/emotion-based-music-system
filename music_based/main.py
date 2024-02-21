from flask import *
from admin import admin
from public import public
from user import user

app = Flask(__name__)
app.register_blueprint(admin)

app.register_blueprint(public)

app.register_blueprint(user)

app.secret_key = 'pro'
app.run(debug=True)

