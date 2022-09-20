import string

import numpy

one = '192.169.0.13'


def is_type():
    if one >= u'\u0030' and one <= u'\u0039':  # 判断是否为ip
        flag = 0
    else:
        flag = 1




uchar = 'www.baidu123.com'
import re
pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)

def is_valid_domain(value):
    """
    Return whether or not given value is a valid domain.
    If the value is valid domain name this function returns ``True``, otherwise False
    :param value: domain string to validate
    """
    return True if pattern.match(value) else False

test = [
    ['地理位置', '乌克兰,文尼察州,文尼察 (planetel.it)', 'AS', '25092 (PE Tetyana Mysyk)', '更新时间', '2020-03-17', 'Tags', 'Web漏洞攻击主机扫描wordpress垃圾邮件恶意软件voip攻击僵尸主机', '开放端口', '22'],
    [''],
    # ['开源情报(407)', '更新时间：2020-03-17'], ['主机扫描'], ['ssh attack'], [''],
    # ['开源情报(477)', '更新时间：2020-03-10'], ['voip攻击'], [''], [''],
    # ['开源情报(407)', '更新时间：2020-03-02'], ['主机扫描Web漏洞攻击'], ['http attackwordpress attackcms attack'], [''],
    ['ns2.cndailynetwork.info'], ['2年前'],
    ['cndailynetwork.info'], ['4年前'],
    ['http://cndailynetwork.info/'], ['10'], ['4年前']
]


def ioc_data():
    ioc = {}
    d = 0
    try:
        for i in test[2: len(test)]:
            if len(i) == 2:
                d = test.index(i)
        t = d  # 判断IOC与头列表的分界值
        new_list = [test[i] for i in range(2, t + 4)]
        data_ioc = numpy.array(list(new_list)).reshape(len(new_list) // 4, 4)
        for j in data_ioc:
            demo = ["update_time", "categories", "families", "organizations"]
            ioc = dict(zip(demo, list(j)))
        print(ioc)
        return t, ioc
    except Exception as e:
        print(e)
        return t, ioc


def domain_data():
    domain = {}
    t = ioc_data()[0]
    b = 0
    if t == 0:
        t = -2
    for j in test[(t + 4): len(test)]:
        for i in j:
            flag = is_valid_domain(i)
        if flag == True:
            b = test.index(j)
    d = b  # d为domain的分割值
    new_list2 = [test[i] for i in range((t + 4), d + 2)]
    data_url = numpy.array(list(new_list2)).reshape(len(new_list2) // 2, 2)
    for i in data_url:
        demo = ["domain", "scan_time"]
        domain = dict(zip(demo, list(i)))
    print(domain)
    return d, domain


def url_data():
    url = {}
    d = domain_data()[0]    # domain分割值
    t = ioc_data()[0]   # ioc分割值
    if t == 0:
        t = -2
    if d == 0:
        d = t + 4
    new_list2 = [test[i] for i in range((d+2), len(test))]
    data_url = numpy.array(list(new_list2)).reshape(len(new_list2) // 3, 3)
    for i in data_url:
        demo = ["url", "threat_score", "scan_time"]
        url = dict(zip(demo, list(i)))
    print(url)
    return url


url_data()
