import functools

from flask import session, g, render_template, redirect, url_for


def login_required(func):
    @functools.wraps(func) # 修饰内层函数，防止当前装饰器去修改被装饰函数的属性
    def inner(*args, **kwargs):
        # 从session获取用户信息，如果有，则用户已登录，否则没有登录
        username = session.get('username')
        # print("session username:", username)
        if not username:
            # WITHOUT_LOGIN是一个常量
            return render_template('login.html',tip=1)
        else:
            # 已经登录的话 g变量保存用户信息，相当于flask程序的全局变量
            g.user_id = username
            return func(*args, **kwargs)

    return inner
