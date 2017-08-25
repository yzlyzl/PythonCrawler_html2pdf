# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# r = requests.get('http://cuiqingcai.com')
# print (type(r))
# print (r.status_code)
# print (r.encoding)
# print (r.cookies)


# params和headers参数
payload = {'key1': 'value1', 'key2': 'value2'} # parameters
headers = {'content-type': 'application/json'}
r = requests.get('http://httpbin.org/get', params = payload,
										   headers = headers) # with params(a dict)
print (r.url)



# r = requests.get("a.json")   ???
# print (r.text)
# print (r.json())



# 获得来自服务器的原始套接字相应
# r = requests.get('https://github.com/timeline.json', stream=True)
# print (r.raw)
# r.raw.read(10)