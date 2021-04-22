from flask import request, render_template, redirect

from . import node  # 蓝图引用进来
from ..user import login_required
from ...dataFun.node import addressNode as data


@node.route('/addresschart')
@login_required
def address():
    return render_template('node/addressNode.html')


def info():
    list=[]
    list.append(request.form.get('province'))
    list.append(request.form.get('city'))
    list.append(request.form.get('area'))
    list.append(request.form.get('detailAddress'))

    return list

@node.route('/asearch',methods=['GET','POST'])
def asearch():
    a=info()
    if a[0] == '' and a[1] == '' and a[2] == '' and a[3] == '':
        return redirect('/general/nodeRes/address')
    else:
        return data.search(a[0],a[1],a[2],a[3])

@node.route('/aadd',methods=['GET','POST'])
def aadd():
    a = info()
    #print(bool(data1.search(kind, name, age, gender, degree, work, home)))

    if bool(data.search(a[0],a[1],a[2],a[3])['nodes']):
        print('fail')
        return "fail"
    else:
        data.add(a[0],a[1],a[2],a[3])
        print('success')
        return "success"

@node.route('/adelete',methods=['GET','POST'])
def adelete():
    id = request.form.get('id')
    a = data.ifdelete(id)

    if a!='noNodes':
        return a
    else:
        a=data.delete(id)
        print(a)
        if len(a['nodes'])==0:
            return 'success'
        else:
            return 'fail'


@node.route('/aupdate',methods=['GET','POST'])
def aupdate():
    id = request.form.get('id')
    #fkind = request.form.get('fkind')
    a = info()
    #print(data1.update(str(id),a[1], a[2], a[3], a[4], a[5], a[6]))

    if data.update(str(id), a[0]):
        return 'success'
    else:
        return 'fail'


