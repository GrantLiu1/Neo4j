from time import time

from flask import render_template, request

from itertools import chain

from . import general #蓝图引用进来

from ..dataFun import data1 as data #数据库查询

@general.route('/nodeRes/<kind>',methods=['GET','POST'])
def nodeRes(kind):
    res= {}
    if kind == 'address':
        str1 = 'match (p)-[r1]->(c)-[r2]->(a)-[r3]->(ad:address) return p,c,a,ad'
    else:
        str1 = 'match (n:'+kind+') return n'
    nodes=data.query_graph(str1)
    #links=data1.query_graph('match (n)-[r]->(m) return r')

    res['nodes']=nodes['nodes']
    res['links']=nodes['links']

    return res

@general.route('/relRes/<kind>',methods=['GET','POST'])
def relRes(kind):
    res= {}

    str1 = 'match (n:'+kind+')-[r]-(m) return n,r,m'
    print(str1)
    res = data.query_graph(str1)
    # categories = []
    # for a in res['nodes']:
    #     if a['label'] not in categories:
    #         categories.append(a['label'])
    # categories=list(chain.from_iterable(categories))
    # res['categories']=categories
    return res

@general.route('/selectAdd',methods=['GET'])
def selectAdd():
    qstr = 'match (n:province)-[r]->(m:city)-[r1]->(q:area) return n,m,q'
    res = data.query_graph(qstr)
    provincelist=[]
    citylist=[]
    arealist=[]

    provinceList=[]

    for a in res['nodes']:
        if a['label'][0] == 'province':
            provincelist.append(a)
        if a['label'][0] == 'city':
            citylist.append(a)
        if a['label'][0] == 'area':
            arealist.append(a)


    for a in provincelist:
        dict1={}
        dict1['name']=a['name']
        dict1['cityList']=[]
        for b in citylist:
            dict2={}
            if b['provinceCode'] == a['code']:
                dict2['name']=b['name']
                dict2['areaList']=[]
            for c in arealist:
                if c['cityCode'] == b['code']:
                    dict2['areaList'].append(c['name'])
            dict1['cityList'].append(dict2)
        provinceList.append(dict1)


    # print(provincelist)
    # print(citylist)
    # print(arealist)

    # print(provinceList)
    res={}
    res['provinceList']=provinceList

    return res