from flask import *
from database import *
import uuid

admin = Blueprint('admin',__name__)

@admin.route('/admin_home')

def adminHome():
    return render_template('admin_page/admin_home.html')

@admin.route('/category',methods=['get','post'])
def category():
    data={}
    q="select * from category"
    p = select(q)
    data['cat']=p
    if 'submit' in request.form:
        cate_list = request.form['cate_list']
        a = "insert into category values(null , '%s' )"%(cate_list)
        s = insert(a)
    return render_template('admin_page/category.html',data=data)

#@admin.route('/category')

# def manC():
#     data = {}
#     q1 = "select * from category"
#     p1 = select(q1)
#     data['view'] = p1

#     return render_template('admin_page/category.html',data=data)

@admin.route('/view_users' , methods = ['get','post'])

def viewuser():
    d = {}
    u = "select * from registration"
    v = select(u)
    d['c'] = v

    return render_template('admin_page/view_user.html',d=d)

@admin.route('/playlist',methods = ['get','post'])

def play():
    if 'submit' in request.form:
       music_name = request.form['mname']
       music_filename = request.files['file']
       path = "static/musics"+str(uuid.uuid1())+music_filename.filename
       music_filename.save(path)
       language = request.form['sel']
       artist_name = request.form['aname']

       query = "insert into playlists values(null , '%s' , '%s' , '%s' , '%s' )"%(music_name,path,language,artist_name)
       a = insert(query)

       return """
                    <script>
                    alert('music enterd successful');
                    window.location='playlist'
                    </script>"""

    return render_template('admin_page/playlist.html')

