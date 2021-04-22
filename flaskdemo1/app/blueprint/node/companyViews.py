from flask import request, render_template

from . import node  # 蓝图引用进来
from ..user import login_required
from ...dataFun.node import companyNode as data, addressNode


@node.route('/companychart')
@login_required
def company():
    return render_template('node/companyNode.html')


def info():
    list=[]
    list.append(request.form.get('category'))
    list.append(request.form.get('name'))
    list.append(request.form.get('location'))
    list.append(request.form.get('mainBusiness'))
    return list

@node.route('/csearch',methods=['GET','POST'])
def csearch():
    a=info()
    return data.search(a[0],a[1])

@node.route('/cadd',methods=['GET','POST'])
def cadd():
    a = info()
    if len(data.search(a[0], a[1])['nodes'])!=0:
        return "hasNode"

    if len(addressNode.searchByDetail(a[2])['nodes'])==0:
        return "noLocation"

    if len(addressNode.ifTaken(a[2]))!=0:
        return "locationHasTaken"

    data.add(a[0],a[1],a[2],a[3])
    return "success"

@node.route('/cdelete',methods=['GET','POST'])
def cdelete():
    id = request.form.get('id')
    a = info()
    print(id)
    if bool(data.search(a[0],a[1])['nodes']):
        if bool(data.delete(str(id))):
            return "success"
        else:
            return "fail"
    else:
        return "fail"

@node.route('/cupdate',methods=['GET','POST'])
def cupdate():
    id = request.form.get('id')
    #fkind = request.form.get('fkind')
    a = info()
    #print(data1.update(str(id),a[1], a[2], a[3], a[4], a[5], a[6]))

    if data.update(str(id), a[0]):
        return 'success'
    else:
        return 'fail'


