#!/usr/bin/python3
import pymysql

global db


def init():
    host = "127.0.0.1"
    username = "root"
    password = "root"
    database = "vinabiz"
    global db
    db = pymysql.connect(host, username, password, database)
    db.set_charset('utf8')


def add_company(data):
    cursor = db.cursor()

    sql = "INSERT INTO vinabiz_company(guid,name,url,a1,a2,a3,a4,a5,a6,a7," \
          "b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,c1,c2,c3,c4,c5,c6)" \
          " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (
              data['guid'], data['name'], data['url'], data['a1'], data['a2'], data['a3'], data['a4'], data['a5'], data['a6'], data['a7'], data['b1'],
              data['b2'],
              data['b3'], data['b4'], data['b5'], data['b6'], data['b7'], data['b8'],
              data['b9'], data['b10'], data['b11'], data['b12'], data['b13'], data['b14'], data['c1'], data['c2'], data['c3'], data['c4'], data['c5'],
              data['c6'])
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e, data)


def get_all_company_url():
    cursor = db.cursor()
    sql = "SELECT url from vinabiz_company "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        url_list = []
        for row in results:
            url_list.append(row[0])
        return url_list
    except Exception as e:
        db.rollback()
        print(e)


def get_all_company_url_by_id(min_id, max_id):
    cursor = db.cursor()
    sql = "SELECT guid,url from vinabiz_company where id>=%d and id<=%d order by id" % (min_id, max_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        list = []
        for row in results:
            data = {}
            data['guid'] = row[0]
            data['url'] = row[1]
            list.append(data)
        return list
    except Exception as e:
        db.rollback()
        print(e)


# 初始化db
init()
