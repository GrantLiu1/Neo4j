from ..data1 import *

def search(idcard, name, age, sex,birthday, education, occupation,company,province,city,area, home,phone,financialSit):
    qstr = "match (n:person) where 1=1 "
    if idcard != '':
        qstr += 'and n.idcard="' + idcard + '" '
    if name != '':
        qstr += 'and n.name="' + name + '" '
    if age != '':
        qstr += 'and n.age="' + age + '" '
    if sex != '':
        qstr += 'and n.sex="' + sex + '" '
    if birthday != '':
        qstr += 'and n.birthday="' + birthday + '" '
    if education != '':
        qstr += 'and n.education="' + education + '" '
    if occupation != '':
        qstr += 'and n.occupation="' + occupation + '" '
    if company != '':
        qstr += 'and n.company="' + company + '" '
    if province != '':
        qstr += 'and n.province="' + province + '" '
    if city != '':
        qstr += 'and n.city="' + city + '" '
    if area != '':
        qstr += 'and n.area="' + area + '" '
    if home != '':
        qstr += 'and n.home="' + home + '" '
    if phone != '':
        qstr += 'and n.phone="' + phone + '" '
    if financialSit != '':
        qstr += 'and n.financialSit="' + financialSit + '" '

    qstr = qstr + ' return n'

    print(qstr)
    return query_graph(qstr)


def searchById(idcard):
    sqtr='match (n:person) where n.idcard="'+idcard+'" return n'
    return query_graph(sqtr)

def add(idcard, name, age, sex,birthday, education, occupation,company,province,city,area, home,phone,financialSit):
    qstr ='merge (n:person{idcard:"'+idcard+'",name:"'+name+'",age:"'+age+'",sex:"'+sex+'",birthday:"'+birthday+'",education:"'+education+\
          '",occupation:"'+occupation+'",company:"'+company+'",province:"'+province+'",city:"'+city+'",area:"'+area+'",home:"'+home+'",phone:"'+phone+\
          '",financialSit:"'+financialSit+'"}) ' \
        'with n ' \
        'match (m:company) ' \
        'match (p:province)-[r1]->(c:city)-[r2]->(a:area)-[r3]->(ad:address) ' \
        'where n.company=m.name and n.province=p.name and n.city=c.name and n.area=a.name and n.home=ad.name ' \
        'with m,ad,n ' \
        'merge (m)-[r4:雇佣]->(n)-[r5:居住]->(ad) '


    print(qstr)

    return query_graph(qstr)


def delete(idcard):
    qstr = 'match (n:person) where n.idcard="'+idcard+'" detach delete n'
    print(qstr)

    query_graph(qstr)

def update(id,name, age, gender, degree, work, home):
    qstr = 'match (n) where id(n)='+id+' '
    setq = 'set n.name="' + name + '" ,n.age=' + age + ' ,n.sex="' + gender + '" ,n.degree="' + degree + '" ,n.work="' + work + '",n.home="' + home + '"  return n'
    # if fkind != kind:
    #     qstr = 'match (n:' + fkind + ') where id(n)='+id+' '
    #     set = 'remove n:'+fkind+' set n:'+kind+''
    # else:
    #     set += 'n.name="'+name+'" ,n.age='+age+' ,n.gender="'+gender+'" ,n.degree="'+degree+'" ,n.work="'+work+'",n.work="'+work+'"  return n'

    qstr += setq

    print(qstr)

    return query_graph(qstr)