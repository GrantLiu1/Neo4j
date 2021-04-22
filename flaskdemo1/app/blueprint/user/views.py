from time import time


from flask import render_template, request
from typing import List

from . import user # 蓝图引用进来
from ...dataFun import data1


def info():
    list=[]
    list.append(request.form.get('kind'))
    list.append(request.form.get('name'))
    list.append(request.form.get('age'))
    list.append(request.form.get('gender'))
    list.append(request.form.get('degree'))
    list.append(request.form.get('work'))
    list.append(request.form.get('home'))

    return list



@user.route('/restext',methods=['GET','POST'])
def restext():
    res= {}
    #start = time()
    nods = data1.query_graph('match (n) return n')
    links = data1.query_graph('match (n)-[r]->(m) return r')
    #end = time()
    #print('查询所有节点关系所需的时间为:'+(end - start))


    res['nodes']=nods['nodes']
    res['links']=links['links']
    # print(nods)
    return res

@user.route('/search',methods=['GET','POST'])
def search():
    a=info()
    return data1.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6])

@user.route('/add',methods=['GET','POST'])
def add():
    # kind = request.form.get('kind')
    # name = request.form.get('name')
    # age = request.form.get('age')
    # gender = request.form.get('gender')
    # degree = request.form.get('degree')
    # work = request.form.get('work')
    # home = request.form.get('home')

    a = info()
    print(a)

    #print(bool(data1.search(kind, name, age, gender, degree, work, home)))

    if bool(data1.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6])['nodes']):
        print(data1.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6])['nodes'])
        print('fail')
        return "fail"
    else:
        data1.add(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        print('success')
        return "success"


@user.route('/delete',methods=['GET','POST'])
def delete():
    a = info()

    if bool(data1.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6])['nodes']):
        #print(data1.search(kind, name, age, gender, degree, work, home)['nodes'])
        data1.delete(a[0], a[1], a[2], a[3], a[4], a[5], a[6])
        print('success')
        return "success"
    else:
        print('fail')
        return "fail"

@user.route('/update',methods=['GET','POST'])
def update():
    id = request.form.get('id')
    #fkind = request.form.get('fkind')
    a = info()


    #print(data1.update(str(id),a[1], a[2], a[3], a[4], a[5], a[6]))

    if(data1.update(str(id), a[1], a[2], a[3], a[4], a[5], a[6])):
        return 'success'
    else:
        return 'fail'

