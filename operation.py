# -*- coding: utf8 -*-
#! python3.8
import json
import numpy
import VE.setup_02
import VE.api


# test = VE.setup_02.start()
test = []

def frist_data():
    data = test[0]
    base_data = {}
    if len(data) % 2 != 0:
        data.append(" ")
        for e in range(0, len(data), 2):
            base_data[data[e]] = data[e + 1]
    return base_data


# 头列表后接的一定是IOC数据表单。return：求出IOC与头表单 的分界值 t 。/组成的ioc字典
def ioc_data():
    d = None
    for i in test[2: len(test)]:
        if len(i) == 2:
            d = test.index(i)
            t = d     # 判断IOC与头列表的分界值
            new_list = [test[i] for i in range(2, t + 4)]
            data_ioc = numpy.array(list(new_list)).reshape(len(new_list)//4, 4)
            for i in data_ioc:
                demo = ["update_time", "categories", "families", "organizations"]
                ioc = dict(zip(demo, list(i)))
                print(ioc)
            return t, ioc


# 求值：IOC与url的分界值
def json_ioc():
    d = None
    t = ioc_data()[0]
    if t == None:
        t = -2
    for j in test[(t + 4): len(test): 3]:
        if "http" in str(j):
            d = test.index(j)
            u = d    # 判断url的分界点值
            new_list2 = [test[i] for i in range((t + 4), u)]
            data_url = numpy.array(list(new_list2)).reshape(len(new_list2)//3, 3)
            for i in data_url:
                demo = ["url", "threat_score", "scan_time"]
                url = dict(zip(demo, list(i)))
                print(url)
            return u, url


def json_md5():
    d = None
    t = ioc_data()[0]
    u = json_ioc()[0]
    if u == None:
        u = t + 4
    new_list3 = [test[i] for i in range((u + 3), len(test))]
    data_md5 = numpy.array(list(new_list3)).reshape(len(new_list3)//3, 3)
    for i in data_md5:
        demo = ["sha256", "threat_score", "scan_time"]
        md5 = dict(zip(demo, list(i)))
        print(md5)
        return md5


def conn_data():
    base_data = frist_data()
    ioc = ioc_data()[1]
    url = json_ioc()[1]
    md5 = json_md5()

    all_data ={
                "version": "01",
                "type": 'ip',
                "data": base_data,
                "ioc": ioc,
                "urls": url,
                "hash": md5,
                "domains": "",
                "ips": ""
            }
    datas = json.dumps(all_data)
    data = {
        "source": "VE",
        "channel": "ip",
        "query_value": "185.198.59.121",
        "json_tags": datas,
        "tags_cont": 1
    }
    # api提交
    # VE.api.get_one(data)
