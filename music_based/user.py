from flask import *
from database import *

user = Blueprint('user',__name__)

@user.route('/user_home')

def userHome():
    return render_template('user_page/user_home.html')