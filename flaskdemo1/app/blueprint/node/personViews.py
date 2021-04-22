from flask import render_template, request

from . import node #蓝图引用进来
from ..user import login_required

from ...dataFun.node import personNode as data, companyNode, addressNode  # 数据库查询

@node.route('/person')
@login_required
def person1():
    
    return 'person'

@node.route('/personchart')
def person():
    return render_template("node/personNode.html")

def info():
    list=[]

    list.append(request.form.get('idcard'))
    list.append(request.form.get('name'))
    list.append(request.form.get('age'))
    list.append(request.form.get('sex'))
    list.append(request.form.get('birthday'))
    list.append(request.form.get('education'))
    list.append(request.form.get('work'))
    list.append(request.form.get('company'))
    list.append(request.form.get('province'))
    list.append(request.form.get('city'))
    list.append(request.form.get('district'))
    list.append(request.form.get('home'))
    list.append(request.form.get('phone'))
    list.append(request.form.get('financialSit'))

    return list


@node.route('/psearch',methods=['GET','POST'])
def search():
    a=info()
    print(a)
    return data.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13])

@node.route('/padd',methods=['GET','POST'])
def padd():
    a = info()
    if len(data.searchById(a[0])['nodes']) != 0:
        return 'hasPerson'

    if len(companyNode.search(a[7])['nodes']) == 0:
        return 'noCompany'

    if len(addressNode.search(a[8],a[9],a[10],a[11])['nodes']) == 0:
        return 'noAddress'

    return data.add(a[0], a[1], a[2], a[3], a[4], a[5], a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13])


@node.route('/pdelete',methods=['GET','POST'])
def pdelete():
    a = info()
    print(a)
    if len(data.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13])['nodes'])!=0:
        data.delete(a[0])
        print('success')
        return "success"
    else:
        print('fail')
        return "fail"

@node.route('/pupdate',methods=['GET','POST'])
def pupdate():
    id = request.form.get('id')
    #fkind = request.form.get('fkind')
    a = info()
    #print(data1.update(str(id),a[1], a[2], a[3], a[4], a[5], a[6]))

    if(data.update(str(id), a[1], a[2], a[3], a[4], a[5], a[6])):
        return 'success'
    else:
        return 'fail'

