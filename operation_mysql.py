#! python3.8
# -*- utf8 -*-
# 从MySQL中获取数据
import MySQLdb


def get_domain_data():
    conn = MySQLdb.Connect(host='localhost', user='root', password='wrh19940',
                           db='db', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select count(*) from domain_ioc where status_v=0')
    count = cursor.fetchone()[0]
    print(count)
    while count > 0:
        select_sql = 'select domain_name from domain_ioc where status_v=0 limit 1'
        cursor.execute(select_sql)
        conn.commit()
        domain = cursor.fetchone()[0]
        cursor.execute('update domain_ioc set status_v=1 WHERE domain_name="{}"' .format(url))
        conn.commit()
        cursor.close()
        conn.close()
        return domain


def get_ip_data():
    conn = MySQLdb.Connect(host='localhost', user='root', password='wrh19940',
                           db='db', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select count(*) from ip_ioc where status_v=0')
    count = cursor.fetchone()[0]
    print(count)
    while count > 0:
        select_sql = 'select ip_name from ip_ioc where status_v=0 limit 1'
        cursor.execute(select_sql)
        conn.commit()
        ip = cursor.fetchone()[0]
        cursor.execute('update ip_ioc set status_v=1 WHERE ip_name="{}"' .format(url))
        conn.commit()
        cursor.close()
        conn.close()
        return ip


def saveInDB(url):
    conn = MySQLdb.Connect(host='localhost', user='root', password='wrh19940',
                           db='crawler', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('insert into ioc_data values(%s,0)' % url)
    conn.commit()


# 通过阈值检查数据库是否需要补货
def checkDB():
    # 从数据库获取一下可用条数
    conn = MySQLdb.Connect(host='localhost', user='root', password='wrh19940',
                           db='crawler', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select count(*) from ioc_data where status=0')
    count = cursor.fetchone()[0]
    if count <= 0:
        print('ico_data 数据库中没有入了！！！！！需要补货了')



