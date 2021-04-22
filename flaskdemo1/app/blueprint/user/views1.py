from flask import render_template, request, session
from typing import List

from . import user #蓝图引用进来
from .decorators import login_required
from ...dataFun import userData as data

@user.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    pwd = request.form.get('pwd')

    if bool(pwd!=data.getpwd(username)[0][0]):
        return '密码错误'
    else:
        session['username']=request.form.get('username')
        session['pwd'] = request.form.get('pwd')
        return '密码正确'



@user.route('/index',methods=['get','post'])
@login_required
def index():
    username = session['username']
    return render_template('index.html',username=username)

@user.route("/chart")
def charts():
    return render_template("node/node.html")

