import json
import time

import neo4j
from py2neo import *

def getGraph():
    return Graph('http://localhost:7474', username='neo4j', password='grant')
    # driver=neo4j.GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'grant'))
    # return driver.session()


def query(str):
    return getGraph().run(str).data()

def query_graph(str):

    data = query(str)

    node_ids = []
    rel_ids=[]
    new_nodes = []
    new_links = []

    for a in data:
        for tk,tv in a.items():
            # nodes = tv.nodes
            #relations = tv.relationships
            # for n in nodes:
            for n in tv.nodes:
                if n.identity in node_ids:
                    continue
                obj = {}
                obj["id"] = n.identity
                obj["label"] = []
                if n.labels is not None:
                    for la in n.labels:
                        obj["label"].append(la)
                for k,v in n.items():
                    obj[k] = v
                new_nodes.append(obj)
                node_ids.append(n.identity)

            # for r in relations:
            for r in tv.relationships:
                if r.identity in rel_ids:
                    continue
                li = {}
                li["id"] = r.identity
                if r.types() is not None:
                    li["label"] = []
                    for la in r.types():
                        li["label"].append(la)
                li["source"] = r.start_node.identity
                li["target"] = r.end_node.identity
                for k, v in r.items():
                    li[k] = v
                rel_ids.append(r.identity)
                new_links.append(li)
    result = {}
    result["nodes"] = new_nodes
    result["links"] = new_links
    return result


def get_nodes(query_str):
    data=query(query_str)

    node_ids = []
    new_nodes = []

    for a in data:
        for tk, tv in a.items():
            for n in tv.nodes:
                if n.identity in node_ids:
                    continue
                obj = {}
                obj["id"] = n.identity
                obj["label"] = []
                if n.labels is not None:
                    for la in n.labels:
                        obj["label"].append(la)
                for k, v in n.items():
                    obj[k] = v
                new_nodes.append(obj)
                node_ids.append(n.identity)

    return new_nodes

def get_links(query_str):
    data = query(query_str)

    rel_ids = []
    new_links = []

    for a in data:
            li = {}
            li["source"] = a['a']
            li["target"] = a['b']
            li["label"] = a['c']
            new_links.append(li)

    return new_links





def toJson(str):

    a = query(str)

    list=[]
    plist = []
    mlist = []

    b = a[0]['n']
    dict_node = {}
    for node in a:
        dict_node=node['n']
        if node['labels(n)'][0]=='Movie':
            dict_node['tag'] = node['labels(n)'][0]
            dict_node['name']=dict_node.pop('title')
        else:
            dict_node['tag'] = node['labels(n)'][0]

        list.append(dict_node)

    return json.dumps(list, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)


# def qur_real(str):



def print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))




if __name__ == '__main__':
    str = 'match (n)-[r]->(m) return r'
    start = time.time()
    data = query(str)
    end = time.time()

    print(end - start)

    print(data)




