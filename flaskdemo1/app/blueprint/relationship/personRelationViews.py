from flask import request, render_template

from . import relationship  # 蓝图引用进来
from ..user import login_required
from ...dataFun.relationship import personRelationship as data


def info():
    list=[]
    list.append(request.form.get('nod1type'))
    list.append(request.form.get('id1'))
    list.append(request.form.get('l1'))
    list.append(request.form.get('relanme'))
    list.append(request.form.get('l2'))
    list.append(request.form.get('nod2type'))
    list.append(request.form.get('id2'))

    return list

@relationship.route('/personchart',methods=['GET'])
@login_required
def personchart():
    relName=data.getrel()
    nodeType= data.getnodeType()
    return render_template('relationship/Relationship.html',relName=relName,nodeType=nodeType)

@relationship.route('/selectperson',methods=['GET','POST'])
@login_required
def selectperson():
    return render_template('relationship/select/selectPerson.html')

@relationship.route('/selectaddress',methods=['GET','POST'])
@login_required
def selectaddress():
    return render_template('relationship/select/selectAddress.html')

@relationship.route('/selectcompany',methods=['GET','POST'])
@login_required
def selectcompany():
    return render_template('relationship/select/selectCompany.html')

@relationship.route('/personrelation')
def personrelation():
    return data.getrel()



@relationship.route('/prSearch',methods=['GET','POST'])
def prSearch():
    a=info()

    if ''==a[2]:
        return 'l1lack'
    if ''==a[4]:
        return 'l2lack'

    a = data.search(a[0], a[1], a[2], a[3], a[4], a[5], a[6])

    if len(a['nodes'])==0:
        return 'noNode'

    return a

@relationship.route('/prAdd',methods=['GET','POST'])
def prAdd():
    a=info()

    return data.add( a[1], a[2], a[3], a[4],a[6])