import neo4j
from time import *
from itertools import chain



def getGraph1():
    return neo4j.GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'grant')).session()

def query(str):
    session =getGraph1()
    a = session.run(str).graph()
    session.close()
    return a

def query_dict(str):
    return getGraph1().run(str).data()


def query_graph(query_str):
    data = query(query_str)

    node_ids = []
    rel_ids = []
    new_nodes = []
    new_links = []

    for node in data.nodes:
        if node._id in node_ids:
            continue
        obj = {}
        obj['id'] = node._id
        obj['label'] = list(node._labels)
        # obj['properties'] = node._properties
        obj.update(dict(node._properties))

        new_nodes.append(obj)
        node_ids.append(node._id)

    for rel in data.relationships:
        if rel._id in rel_ids:
            continue
        link = {}
        link['id'] = rel._id
        link['label'] = rel.type
        link['properties'] = rel._properties
        link['source'] = str(rel.start_node._id)
        link['target'] = str(rel.end_node._id)
        new_links.append(link)
        rel_ids.append(rel._id)

    # print(new_nodes)
    # print(new_links)
    result = {}
    result['nodes'] = new_nodes
    result['links'] = new_links

    return result

def search(kind, name, age, gender, degree, work, home):
    str = "match (n) where 1=1 "
    if kind != '':
        str = 'match (n:' + kind + ') where 1=1 '
    if name != '':
        str += 'and n.name="' + name + '" '
    if age != '':
        str += 'and n.age=' + age + ' '
    if gender != '':
        str += 'and n.sex="' + gender + '" '
    if degree != '':
        str += 'and n.degree="' + degree + '" '
    if work != '':
        str += 'and n.work="' + work + '" '
    if home != '':
        str += 'and n.home="' + home + '" '

    str = str + ' return n'

    print(str)
    return query_graph(str)


def add(kind, name, age, gender, degree, work, home):
    str = "merge (n{"
    if kind != '':
        str = 'merge (n:' + kind + '{'
    if name != '':
        str += 'name:"' + name + '" '
    if age != '':
        str += ',age:' + age + ' '
    if gender != '':
        str += ' ,sex:"' + gender + '" '
    if degree != '':
        str += ' ,degree:"' + degree + '" '
    if work != '':
        str += ' ,work:"' + work + '" '
    if home != '':
        str += ' ,home:"' + home + '" '
    str = str + '})'

    print(str)

    query_graph(str)


def delete(kind, name, age, gender, degree, work, home):
    str = "match (n) where 1=1 "
    if kind != '':
        str = 'match (n:' + kind + ') where 1=1 '
    if name != '':
        str += 'and n.name="' + name + '" '
    if age != '':
        str += 'and n.age=' + age + ' '
    if gender != '':
        str += 'and n.sex="' + gender + '" '
    if degree != '':
        str += 'and n.degree="' + degree + '" '
    if work != '':
        str += 'and n.work="' + work + '" '
    if home != '':
        str += 'and n.home="' + home + '" '

    str += ' detach delete n'

    print(str)

    query_graph(str)

def update(id,name, age, gender, degree, work, home):
    str = 'match (n) where id(n)='+id+' '
    set = 'set n.name="' + name + '" ,n.age=' + age + ' ,n.sex="' + gender + '" ,n.degree="' + degree + '" ,n.work="' + work + '",n.home="' + home + '"  return n'
    # if fkind != kind:
    #     str = 'match (n:' + fkind + ') where id(n)='+id+' '
    #     set = 'remove n:'+fkind+' set n:'+kind+''
    # else:
    #     set += 'n.name="'+name+'" ,n.age='+age+' ,n.gender="'+gender+'" ,n.degree="'+degree+'" ,n.work="'+work+'",n.work="'+work+'"  return n'

    str += set

    print(str)

    return query_graph(str)

if __name__ == '__main__':
    # str1 = 'match (n)-[r]->(m) return r'
    #
    # str1 = 'match (n) return n '
    # print(len(query_graph(str1)['nodes']))
    # end=time()
    # print(end-start)
    #print(add("P", "l1", "11", "学士", ))
    str1='match (n:person)-[r]-(m) return n,r,m'
    res=query_graph(str1)
    cate=[]
    for a in res['nodes']:
        if a['label'] not in cate:
            cate.append(a['label'])
    print(cate)
    print(list(chain.from_iterable(cate)))
