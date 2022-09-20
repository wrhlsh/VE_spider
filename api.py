import json

import requests


def get_one(data):
    res = requests.post(url="http://192.168.105.121:8888/article/tag_channel/", data=data)
    print(res.json)


'''
{
        "source": "VE",
        "channel": "ip",
        "query_value": "185.198.59.121",
        "json_tags": datas,
        "tags_cont": 1
    }
'''


def get_all_data(data):
    res = requests.post(url='http://192.168.105.121:8888/docking/origin_data/', data=data)
    print(res.json)


'''
{
    "title":"标题",
    "url":"文件的url",
    "content":"文件的内容。。。。。。。。。。。。。。。",
    "suffix":"文件后缀名"
}
'''


def get_tags(data):
    res = requests.post(url='http://192.168.105.121:8888/docking/tag_model/', data=data)
    print(res.json)


'''
{
	"name": "远程木马",
    "source": "微步"
}
'''


def get_connection_tags(data):
    res = requests.post(url='http://192.168.105.121:8000/article/tag_channel/', data=data)
    print(res.json)


'''
{
	"source": "微步、VE、奇安信、IBM、绿盟",
    "tag_name": "木马",
    "channel":"domin",
    "content": "123.12.54.22",
}
'''
all_data ={
    'version': '01',
    'type': 'ip',
    "data":
        {
            "name": "193.201.224.28",
            "registrar": " ",
            "cy": "乌克兰", "provincial": "文尼察州",
            "aso": "PE Tetyana Mysyk",
            "domain_main": " ",
             "tags": [{"Web漏洞攻击": "red"}, {"主机扫描": "yellow"}],

    "ioc": [
            {
            "categories": [{"Web漏洞攻击": "blue"}, {"主机扫描": "blue"}],
            "families": ["ssh attack", "sshd attack"],
            "organizations": ["APT32"],
            "update_time": 1552233600
            },
            {
            "categories": ["主机扫描", "可疑"],
            "families": ["ssh attack", "sshd attack"],
            "organizations": ["APT32"],
            "update_time": 1552233600
            }
            ],

    "urls": [

            {
            "url": "http://185.198.59.121/old/xp.exe",
            "threat_score": 100,
            "scan_time": 1571515049
            }
            ],
    "hash":
            [
            {
            "sha256": "0a26ce94a73c224e5ffed3f6f1f98163176a9e6da9f28813bfd51be370b7ff4a",
            "threat_score": 100,
            "scan_time": 1571853775
            }
            ],
    "domains":
            [
            {
            "resolve_time": 1521216000,
            "domain": "ns2.cndailynetwork.info"
            }
            ],
    "ips":

            [{"country_code": "NL", "update_time": 1541975106, "ip": "193.169.245.137"}]
        }
    }
datas = json.dumps(all_data)
data = {
        "source": "VE",
        "channel": "ip",
        "query_value": "185.198.59.121",
        "json_tags": datas,
        "tags_cont": ''
    }
get_one(data)










