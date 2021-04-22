import pymysql

def mysqlexe(qstr):
    db = pymysql.connect(user='root', password='root', database='neo4juser', charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(qstr)
        res = cursor.fetchall()
        return res
    except:
        print("Error: unable to fetch data")

    finally:
        db.close()

def getpwd(username):
    qstr='select user.pwd from user where user.username="'+str(username)+'"'
    print(qstr)
    res = mysqlexe(qstr)
    return res

if __name__ == '__main__':

    res = mysqlexe("select * from user")
    for row in res:
        for info in row:
            print(info)
