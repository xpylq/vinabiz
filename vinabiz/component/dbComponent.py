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
    if not data.__contains__('office_address'):
        data['office_address'] = ''
    if not data.__contains__('phone1'):
        data['phone1'] = ''
    if not data.__contains__('fax'):
        data['fax'] = ''
    if not data.__contains__('email'):
        data['email'] = ''
    if not data.__contains__('website'):
        data['website'] = ''
    if not data.__contains__('representative'):
        data['representative'] = ''
    if not data.__contains__('phone2'):
        data['phone2'] = ''
    if not data.__contains__('representative_address'):
        data['representative_address'] = ''
    if not data.__contains__('manager'):
        data['manager'] = ''
    if not data.__contains__('phone_director'):
        data['phone_director'] = ''
    if not data.__contains__('address_director'):
        data['address_director'] = ''
    if not data.__contains__('accountant'):
        data['accountant'] = ''
    if not data.__contains__('phone_accounting'):
        data['phone_accounting'] = ''
    if not data.__contains__('account_address'):
        data['account_address'] = ''

    sql = "INSERT INTO vinabiz_company(guid,url,official_name,trading_name,business_code,date_range,tax_authorities_manage,date_of_commencement_of_operation,status," \
          "office_address,phone1,fax,email,website,representative,phone2,representative_address,manager,phone_director,address_director,accountant,phone_accounting," \
          "account_address,main_job,economic_field,type_of_economic,type_of_organization,class_chapters,item_type)" \
          " VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (
              data['guid'], data['url'], data['official_name'], data['trading_name'], data['business_code'],
              data['date_range'], data['tax_authorities_manage'],
              data['date_of_commencement_of_operation'], data['status'], data['office_address'],
              data['phone1'], data['fax'], data['email'], data['website'], data['representative'], data['phone2'],
              data['representative_address'],
              data['manager'], data['phone_director'], data['address_director'], data['accountant'],
              data['phone_accounting'], data['account_address'],
              data['main_job'], data['economic_field'],
              data['type_of_economic'], data['type_of_organization'], data['class_chapters'],
              data['item_type'])
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


def get_all(min_id, max_id):
    cursor = db.cursor()
    sql = "SELECT id,guid,url,official_name,trading_name,business_code,date_range,tax_authorities_manage," \
          "date_of_commencement_of_operation,status,office_address,phone1,fax,email,website,representative,phone2," \
          "representative_address,manager,phone_director,address_director,accountant,phone_accounting,account_address," \
          "main_job,economic_field,type_of_economic,type_of_organization,class_chapters,item_type from vinabiz_company where id>=%d and id<=%d order by id" % (
              min_id, max_id)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        list = []
        for row in results:
            data = {}
            data['id'] = str(row[0])
            data['guid'] = row[1]
            data['url'] = row[2]
            data['official_name'] = row[3]
            data['trading_name'] = row[4]
            data['business_code'] = row[5]
            data['date_range'] = row[6]
            data['tax_authorities_manage'] = row[7]
            data['date_of_commencement_of_operation'] = row[8]
            data['status'] = row[9]
            data['office_address'] = row[10]
            data['phone1'] = row[11]
            data['fax'] = row[12]
            data['email'] = row[13]
            data['website'] = row[14]
            data['representative'] = row[15]
            data['phone2'] = row[16]
            data['representative_address'] = row[17]
            data['manager'] = row[18]
            data['phone_director'] = row[19]
            data['address_director'] = row[20]
            data['accountant'] = row[21]
            data['phone_accounting'] = row[22]
            data['account_address'] = row[23]
            data['main_job'] = row[24]
            data['economic_field'] = row[25]
            data['type_of_economic'] = row[26]
            data['type_of_organization'] = row[27]
            data['class_chapters'] = row[28]
            data['item_type'] = row[29]
            list.append(data)
        return list
    except Exception as e:
        db.rollback()
        print(e)


# 初始化db
init()
