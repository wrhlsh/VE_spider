import time
import random
import pymysql
import unittest
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from mysql_ceshi import get_url

BORDER = 6


class CrackGeetest():
    def __init__(self):
        self.url = url
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    # 打开网页
    def open(self):
        self.browser.get(self.url)

    # 关闭网页
    def close(self):
        self.browser.close()
        self.browser.quit()

    # 确认页面是否打开
    def is_open_page(self):
        search = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'venusScahe'))

        )
        return search

    # enter键
    def enter(self):
        self.browser.find_element_by_id('venusScahe').send_keys(Keys.RETURN)

    # 输入IOC数据，进行查询
    def input_data(self):
        self.browser.find_element_by_id('venusScahe').send_keys(one)
        self.enter()

    # 确认整个页面全部信息是否加载完成
    def is_get_htmml(self):
        first = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'title'))
        )
        return first

    #  该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def isElementExist(self, element):
        flag = True
        try:
            self.browser.find_element_by_css_selector(element)
            return flag
        except:
            flag = False
            return flag

    # 获取整个页面的所有信息
    def get_html(self):
        flag = self.isElementExist("ipscon")
        if flag == 'True':
            content = self.browser.find_element_by_id('ipscon').text
        else:
            content = self.browser.find_element_by_id('Domain').text
        print(content)
        # api接口
        data = {
            "title": one,
            "url": "https://www.venuseye.com.cn/",
            "content": content,
            "suffix": "txt"
        }

    def get_source_html(self):
        html = self.browser.execute_script("return document.documentElement.outerHTML")
        print(html)

    def get_part_data(self):

        element = ''
        flag = self.isElementExist(element)
        if flag == 'True':
            ioc_list = self.browser.find_element_by_css_selector(
                '#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > div > div >'
                ' table').text
            print(ioc_list)
        else:
            ioc_list = self.browser.find_element_by_css_selector(
                '#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > div > div >'
                ' table')
            tags = ioc_list.value_of_css_property('red-tag')
            print(tags)

    # 获取第一个列表的所有数据
    def condensed_list(self):
        try:
            list1 = self.browser.find_element_by_css_selector('#Domain > div.container.fadeIn > div.domain-header >'
                                                              ' div > div > table').text
            print(list1)
        except:
            list1 = self.browser.find_element_by_css_selector('#ipscon > div.container.fadeIn > div.domain-header >'
                                                              ' div > div > table').text
            print(list1)

    # 获取IOC的主要信息
    def ioc_vertical(self):
        # ioc_list1 = str(ioc_list).split('\n')
        try:

            flag = self.isElementExist("#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > "
                                       "div > div > table")
            if flag == 'True':
                ioc_list = self.browser.find_element_by_css_selector(
                    '#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > div > div >'
                    ' table').text
                print(ioc_list)
            else:
                pass
        except:
            flag = self.isElementExist(
                "#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > div > div > table")
            if flag == 'True':
                ioc_list = self.browser.find_element_by_css_selector(
                    '#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(2) > div > div > table').text
                print(ioc_list)
            else:
                pass

    def url_vertical(self):
        try:
            flag = self.isElementExist(
                "#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(10) > div:nth-child(1) > div > table")
            if flag == 'True':
                urls_list = self.browser.find_element_by_css_selector(
                    '#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(10) > div:nth-child(1) > div > table').text
                print(urls_list)
            else:
                pass
        except:
            flag = self.isElementExist(
                "#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(10) > div:nth-child(1) >"
                " div > table")
            if flag == 'True':
                urls_list = self.browser.find_element_by_css_selector(
                    '#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(10) >'
                    ' div:nth-child(1) > div > table').text
                print(urls_list)
            else:
                pass

    def ip_vertical(self):
        try:
            flag = self.isElementExist(
                "#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) > div:nth-child(1) >"
                " div > table")
            if flag == 'True':
                ip_list = self.browser.find_element_by_css_selector('#Domain > div.container.fadeIn > div.domain-tab-content > '
                                                                'div:nth-child(4) > div > div > table').text
                print(ip_list)
            else:
                pass
        except:
            flag = self.isElementExist(
                "#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) > div > div > table")
            if flag == 'True':
                ip_list = self.browser.find_element_by_css_selector(
                    '#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) > div > div > table').text
                print(ip_list)
            else:
                pass

    def md5_vertical(self):
        try:
            flag = self.isElementExist(
                "#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(10) >"
                " div:nth-child(2) > div > table")
            if flag == 'True':
                md5_list = self.browser.find_element_by_css_selector(
                    '#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(10)'
                    ' > div:nth-child(2) > div > table').text
                print(md5_list)
        except:
            flag = self.isElementExist(
                "#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) > div:nth-child(3) > div > table")
            if flag == 'True':
                md5_list = self.browser.find_element_by_css_selector(
                    '#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) >'
                    ' div:nth-child(3) > div > table').text
                print(md5_list)

    def domain_vertical(self):
        try:
            flag = self.isElementExist(
                "#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(6) >"
                " div:nth-child(3) > div > table")
            if flag == 'True':
                domain_list = self.browser.find_element_by_css_selector(
                    '#Domain > div.container.fadeIn > div.domain-tab-content > div:nth-child(6) >'
                    ' div:nth-child(3) > div > table').text
                print(domain_list)
        except:
            flag = self.isElementExist(
                "#ipscon > div.container.fadeIn > div.domain-tab-content > div:nth-child(4) >"
                " div:nth-child(1) > div > table")
            if flag == 'True':
                domain_list = self.browser.find_element_by_css_selector(
                    '#ipscon > div.container.fadeIn > div.domain-tab-content >'
                    ' div:nth-child(4) > div:nth-child(1) > div > table').text
                print(domain_list)

    def start(self):
        start_time = time.time()
        self.open()
        self.is_open_page()
        self.input_data()
        self.is_get_htmml()
        # self.get_html()
        self.get_source_html()
        # self.get_part_data()
        # self.condensed_list()
        # self.ioc_vertical()
        # self.url_vertical()
        # self.ip_vertical()
        # self.md5_vertical()
        # self.domain_vertical()
        self.close()
        end = time.time()
        long_time = end - start_time
        print('执行一次所需的时间为：', long_time)



if __name__ == '__main__':
    one = '91.229.79.184'
    url = 'https://www.venuseye.com.cn/'
    crack = CrackGeetest()
    crack.start()



