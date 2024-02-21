from flask import *
from database import *
import uuid

public = Blueprint('public',__name__)

@public.route('/')

def publicHome():
    return render_template('home.html')

@public.route('/login',methods=['get','post'])

def logins():
    if 'submit' in request.form :
        username = request.form['name']
        password = request.form['password']

        q = "select * from login where username = '%s' and password = '%s' "%(username,password)
        res = select(q)

        if res:
            session['login_id'] = res[0]['login_id'] #reptition avishyam ola line aanu
            if res[0]['user_type'] == 'admin':
                return """
                    <script>
                    alert('login successful');
                    window.location='admin_home'
                    </script>"""
            
            elif res[0]['user_type'] == 'user':
                q2 = "select * from registration where login_id = '%s' "%(session['login_id'])
                res1 = select(q2)
                if res1:
                    session['user_id'] = res1[0]['user_id']
                    return """
                    <script>
                    alert('login successful');
                    window.location='user_home'
                    </script>"""

                return redirect("user_home")

    return render_template('login.html')

@public.route('/register',methods=['get','post'])

def user_lo():
    if 'submit' in request.form:
        name = request.form['txt']
        username = request.form['name']
        password = request.form['password']
        Address = request.form['area']
        city = request.form['city']
        pincode = request.form['pincode']
        email = request.form['mail1']
        gender = request.form['gen']
        language = request.form['sel']
        nationality = request.form['nat']
        profile_pic = request.files['img1']
        path = "static/user"+str(uuid.uuid1())+profile_pic.filename
        profile_pic.save(path)
        age = request.form['age']
        state = request.form['state']
        date_o_birth = request.form['dob']
        phonenumber = request.form['num']

        # if password == password1:
        #     pass

        q2 = "insert into login values(null,'%s','%s','user' )"%(username,password)
        rec = select(q2)
            
        
        q3 = "insert into registration values(null , '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name , Address , city, pincode , email ,gender, language ,nationality,path,rec,age,state,date_o_birth,phonenumber)
        rec1 = insert(q3)

        
        return redirect("user_home")

    return render_template('registration.html')
