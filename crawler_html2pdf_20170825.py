# Problem: Using crawler to get content from html to pdf

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import re
import time

try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

import 
import requests
from bs4 import BeautifulSoup

class Crawler(object):
    """ 爬虫基类 """

    def __init__(self, name, start_url):
        """ 初始化 
            : param name: 要保存的pdf文件的名称
            : param start_url: 爬虫入口URL
        """
        self._name = name
        self._start_url = start_url
        # ???
        self._domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self._start_url))
        
    @staticmethod    # ???
    def request(url, **kw):
        """ 网络请求
            返回response对象
        """
        response = requests.get(url, **kw)
        return response

    def parse_menu(self, response):
        """
            从response中解析出所有目录的URL链接
        """
        raise NotImplementedError

    def parse_body(self, response):
        """
            解析正文，返回经过处理的html文本
        """
        raise NotImplementedError

    def run(self):
        """
            执行爬虫操作，生成pdf文件
        """
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

        htmls = []
        urls = self.parse_menu(self.request(self._start_url))
        # 将所有目录的url分别解析，并将每页正文部分分别写入一个HTML文件
        for index, url in enumerate(urls):
            html = self.parse_body(self.request(url))
            f_name = '.'.join([str(index), 'html'])
            with open(f_name, 'wb') as f:
                f.write(html)
            htmls.append(f_name)

        # 将HTML文件通过pdfkit转换为PDF文件
        pdfkit.from_file(htmls, self._name + '.pdf', options=options)
        for html in htmls:
            os.reomve(html)


class LiaoxuefengPythonCrawler(Crawler):
    """
       针对LiaoXue Feng博客的Python教程的爬虫类
    """
    def parse_menu(self, response):
        """
            从response中解析出所有目录的URL链接
            返回URL生成器
        """
        soup = BeautifulSoup(response.content, 'lxml')
        menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
        for li in menu_tag.find_all('li'):
            url = li.a.get('href')
            if not url.startswith('http'):    # 补全路径
                url = ''.join([self._domain, url])
            yield url

    def parse_body(self, response):
        """
            解析正文，返回经过处理的html文本
        """
        soup = BeautifulSoup(response.content, 'lxml')
        body = soup.find_all(class_="x-wiki-content")[0]
        html = str(body)
        html = html_template.format(content=html)    # 扩展正文为完整的HTML代码
        html = html.encode('utf-8')
        return html



if __name__ == '__main__':
	start_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
	crawler = LiaoxuefengPythonCrawler("廖雪峰Python教程", start_url)
	crawler.run()

