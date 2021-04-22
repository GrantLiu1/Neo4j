from ..data1 import *

def search(category,name):
    qstr = "match (n:company) where 1=1 "
    if category != '':
        qstr += 'and n.category="' + category + '" '
    if name != '':
        qstr += 'and n.name="' + name + '" '

    qstr = qstr + ' return n'

    print(qstr)
    return query_graph(qstr)

def add(category,name,location,mainBusiness):
    qstr = 'merge (n:company{'\
        'name:"' + name + '", ' \
        'category:"'+category+'",' \
        'location:"'+location+'",' \
        'mainBusiness:"'+mainBusiness+'"' \
        '})  return n'
    print(qstr)
    return query_graph(qstr)

def delete(id):
    print(id)
    qstr = "match (n:company) where 1=1 "
    if id != '':
        qstr += 'and id(n)='+id+' '
    else:
        return False
    qstr += ' detach delete n'

    print(qstr)
    return query_graph(qstr)


def update(id,name):
    qstr = 'match (m)-[r:雇佣]-(n:company) where id(n)='+id+' return r'
    if len(query_graph(qstr)['nodes'])==0:
        qstr = 'match (n:company) where id(n)='+id+' '
        setq = 'set n.name="' + name + '" return n'
    else:
        qstr = 'match (m)-[r:雇佣]-(n:address) where id(n)=' + id + ' '
        setq = 'set n.name="' + name + '",m.home="' + name + '"  return n'

    # str = 'match (m)-[r:居住]-(n:address) where id(n)='+id+' '
    # set = 'set n.name="' + name + '",m.home="'+name+'"  return n'
    # if fkind != kind:
    #     str = 'match (n:' + fkind + ') where id(n)='+id+' '
    #     set = 'remove n:'+fkind+' set n:'+kind+''
    # else:
    #     set += 'n.name="'+name+'" ,n.age='+age+' ,n.gender="'+gender+'" ,n.degree="'+degree+'" ,n.work="'+work+'",n.work="'+work+'"  return n'

    qstr += setq
    print(qstr)
    return query_graph(qstr)


