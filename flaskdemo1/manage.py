from datetime import timedelta

from flask import Flask, render_template, session, redirect
from app.blueprint import general
from app.blueprint.node import node
from app.blueprint.relationship import relationship

from app.blueprint.user import user



# 循环引用，解决方法，推迟一方的导入，让另外一方完成
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=5)
app.secret_key = 'lll'
# 注册蓝图（注册goods模块下的蓝图对象，就可以访问相应的路径）
app.register_blueprint(general, url_prefix='/general')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(node, url_prefix='/node')
app.register_blueprint(relationship, url_prefix='/relationship')



@app.route('/')
def index():
    username = session.get('username')
    if username is not None:
        return redirect('user/index')
    return render_template("login.html",tip=0)


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0', debug=True)