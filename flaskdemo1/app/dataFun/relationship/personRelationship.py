from ..data1 import *
from ..commonFunction import *

def getrel():
    qstr = 'match (n)-[r]-(m) return distinct(type(r))'
    res = query_dict(qstr)
    typelist = []
    for a in res:
        typelist.append(a['(type(r))'])
        #print(a['(type(r))'])

    return typelist

def getnodeType():
    return getndoeType()

def search(nod1type,id1,l1,relanme,l2,nod2type,id2):



    if '' != nod1type:
        qstr = 'match (n:'+nod1type+') '
    else:
        qstr = 'match (n) '

    if '' != l1:
        qstr += l1
    else:
        qstr += '-'

    if '' != relanme:
        qstr += ('[r:'+relanme+']')
    else:
        qstr += '[r]'

    if '' != l2:
        qstr += l2
    else:
        qstr += '-'

    if '' != nod2type:
        qstr += ('(m:'+nod2type+') ')
    else:
        qstr += '(m)'

    qset = 'where 1=1'

    if '' != id1:
        qset += ' and id(n)='+id1+' '

    if '' != id2:
        qset += ' and id(m)='+id2+' '

    qstr += qset

    qstr += ' return n,r,m'

    print(qstr)
    return query_graph(qstr)

# def existNode1(node1name,node1age,node1sex):
#     qstr = 'match (n:person) where n.name="'+node1name+'" and n.age='+node1age+' and n.sex="'+node1sex+'" return n'
#     return query_graph(qstr)
#
# def existNode2(node2name):
#     qstr = 'match (n) where n.name="'+node2name+'" return n'
#     return query_graph(qstr)

def add(nod1type,id1,l1,relanme,l2,nod2type,id2):
    qstr1 = 'match (n:'+nod1type+') where id(n)='+id1+' '
    qstr2 = 'match (m:'+nod2type+') where  d(n)='+id2+' '
    qstr3 = 'merge (n)'+l1+'[r:'+relanme+']'+l2+'(m) return n,r,m'
    qstr = qstr1+qstr2+qstr3

    print(qstr)
    return query_graph(qstr)
