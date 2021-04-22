from ..data1 import *

def searchByDetail(address):
    qstr = 'match (n:address) where n.name="'+address+'" return n'
    return query_graph(qstr)
def ifTaken(address):
    qstr = 'match (m:company)-[r:位于]->(n:address) where n.name="'+address+'" return r'
    return query_graph(qstr)['links']

def search(province,city,area,detailAddress):
    if province=='' and city=='' and area=='' and detailAddress=='':
        qstr = "match (n:address) "
        print(qstr)
        return query_graph(qstr)
    else:
        qstr = 'match (p)-[r1]->(c)-[r2]->(a)-[r3]->(ad:address) where 1=1 '
        returnstr=' return 1'
        if province != '':
            qstr += 'and p.name="' + province + '" '
            returnstr += ',p,r1,c'
        if city != '':
            qstr += 'and c.name="' + city + '" '
            returnstr += ',r2,a'
        if area != '':
            qstr += 'and a.name="' + area + '" '
            returnstr += ',r3,ad'
        if detailAddress != '':
            qstr += 'and ad.name="' + detailAddress + '" '
            #returnstr += ',ad'

        qstr+=returnstr
        print(qstr)
        res = query_graph(qstr)
        print(res)
        return res

def add(province,city,area,detailAddress):

    qstr = 'match (p:province)-[r1]->(c:city)-[r2]->(a:area) where p.name="'+province+'" and c.name="'+city+'" and a.name="'+area+'" with p,c,a merge (a)-[r:管辖]->(addr:address{name:"'+detailAddress+'",paddr:a.name})'

    print(qstr)

    return query_graph(qstr)

def delete(id):
    print(id)
    qstr = "match (n:address) where 1=1 "
    if id != '':
        qstr += 'and id(n)='+id+' '
    else:
        return False
    qstr += ' detach delete n'

    print(qstr)
    return query_graph(qstr)


def ifdelete(id):
    qstr = 'match (m)-[r]->(n) where id(m)='+id+' return n'
    print(qstr)
    if len(query_graph(qstr)['nodes'])!=0:
        return 'hasNodes'
    else:
        return 'noNodes'


