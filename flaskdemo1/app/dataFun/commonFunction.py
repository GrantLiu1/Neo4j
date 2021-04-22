from app.dataFun.data1 import query_dict


def getndoeType():
    qstr = 'match (n) return distinct(labels(n))'
    res = query_dict(qstr)
    typelist = []
    for a in res:
        typelist.append(a['(labels(n))'])

    return typelist