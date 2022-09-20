#! python3.8
# -*- utf8 -*-
# 主要处理ip
import json
import re
import time
import random
import numpy
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from .operation_mysql import get_ip_data
# import VE.api



BORDER = 6
# one = get_ip_data()
one = '91.229.79.184'
url = 'https://www.venuseye.com.cn/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
wait = WebDriverWait(browser, 30)


# 打开网页
def open():
    browser.get(url)


# 关闭网页
def close():
    browser.close()
    browser.quit()


# 确认页面是否打开
def is_open_page():
    search = wait.until(
        EC.element_to_be_clickable((By.ID, 'venusScahe'))

    )


# enter键
def enter():
    browser.find_element_by_id('venusScahe').send_keys(Keys.RETURN)


# 输入IOC数据，进行查询
def input_data():
    browser.find_element_by_id('venusScahe').send_keys(one)
    enter()


# 确认整个页面全部信息是否加载完成
def is_get_htmml():
    first = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'title'))
    )
    return first


#  该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def is_type():
    if one >= u'\u0030' and one <= u'\u0039':  # 判断是否为ip
        flag = 'True'
    else:
        flag = 'False'
    return flag


# 获取整个页面的所有信息
def get_html():
    flag = is_type()
    if flag == 'True':
        content = browser.find_element_by_id('ipscon').text
    else:
        content = browser.find_element_by_id('Domain').text
    # api接口
    data = {
        "title": one,
        "url": "https://www.venuseye.com.cn/",
        "content": content,
        "suffix": "txt"
    }


def start():
    open()
    is_open_page()
    input_data()
    time.sleep(random.randint(1, 2))
    is_get_htmml()
    # 获取源html信息
    html = browser.execute_script("return document.documentElement.outerHTML")
    ele = etree.HTML(html)
    try:
        tags_attr = ele.xpath(
            '//*[@id="ipscon"]/div[2]/div[1]/div/div/table/tbody/tr/td[1]/div/dl[4]/dd/span/@class')
        print(tags_attr)
# //*[@id="Domain"]/div[2]/div[1]/div/div/table/tbody/tr/td[1]/div/dl[5]/dd/span/text()
        tags = ele.xpath('//*[@id="ipscon"]/div[2]/div[1]/div/div/table/tbody/tr/td[1]/div/dl[4]/dd/span/text()')
        print(tags)
        tag = dict(zip(tags, tags_attr))
        print(tag)
    except:
        print('没有tags值')
    # 获取全部页面的表单,返回值：页面全部的表单信息，其中包括IOC，domain，url，hash，ip
    row = browser.find_elements_by_tag_name('tr')
    list = []
    for i in row:
        j = i.find_elements_by_tag_name('td')
        for item in j:
            text = item.text
            list.append(text)
    list2 = []
    for i in list:
        list2.append(i.split('\n'))
    close()
    # print(list2)
    return list2


class ToolsData:


    def is_valid_domain(self,value):
        """
        Return whether or not given value is a valid domain.
        If the value is valid domain name this function returns ``True``, otherwise False
        :param value: domain string to validate
        """
        return True if pattern.match(value) else False

    def get_header(self):
        data = test[0]
        base_data = {}
        if len(data) % 2 != 0:
            data.append(" ")
            for e in range(0, len(data), 2):
                base_data[data[e]] = data[e + 1]
        else:
            for e in range(0, len(data), 2):
                base_data[data[e]] = data[e + 1]
        # print(base_data)
        return base_data

    # 头列表后接的一定是IOC数据表单。return：求出IOC与头表单 的分界值 t  //组成的ioc字典
    def ioc_data(self):
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
            # print(ioc)
            return t, ioc
        except Exception as e:
            print(e)
            return t, ioc

    def domain_data(self):
        domain = {}
        t = self.ioc_data()[0]
        b = 0
        if t == 0:
            t = -2
        for j in test[(t + 4): len(test)]:
            for i in j:
                flag = self.is_valid_domain(i)
            if flag == True:
                b = test.index(j)
        d = b  # d为domain的分割值
        new_list2 = [test[i] for i in range((t + 4), d + 2)]
        data_url = numpy.array(list(new_list2)).reshape(len(new_list2) // 2, 2)
        for i in data_url:
            demo = ["domain", "scan_time"]
            domain = dict(zip(demo, list(i)))
        # print(domain)
        return d, domain

    def url_data(self):
        url = {}
        d = self.domain_data()[0]  # domain分割值
        t = self.ioc_data()[0]  # ioc分割值
        if t == 0:
            t = -2
        if d == 0:
            d = t + 4
        new_list2 = [test[i] for i in range((d + 2), len(test))]
        data_url = numpy.array(list(new_list2)).reshape(len(new_list2) // 3, 3)
        for i in data_url:
            demo = ["url", "threat_score", "scan_time"]
            url = dict(zip(demo, list(i)))
        # print(url)
        return url

    def db_insert(self):
        base_data = self.get_header()
        ioc = self.ioc_data()[1]
        domain = self.domain_data()[1]
        url = self.url_data()
        datas = {
            "version": "01",
            "type": 'ip',
            "name": one,
            "data": base_data,
            "ioc": ioc,
            "domain": domain,
            "urls": url,
        }
        data = {
        "source": "VE",
        "channel": "ip",
        "query_value": one,
        "json_tags": json.dumps(datas),
        "tags_cont": ''
        }
        # VE.api.get_one(data)



if __name__ == '__main__':
    pattern = re.compile(
        r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
        r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
    )
    tools = ToolsData()
    start_time = time.time()
    test = start()
    tools.db_insert()
    end_time = time.time()
    long_time = end_time - start_time
    print('执行一次所需时长为：', long_time)