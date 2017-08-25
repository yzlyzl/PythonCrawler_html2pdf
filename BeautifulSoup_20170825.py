# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import bs4

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
# print (soup.prettify())    # 格式化输出



# ##Tag
# print (soup.title)
# print (soup.head)
# print (soup.a)
# print (soup.p)

# # name attribute for Tag
# print (soup.name)
# print (soup.head.name)
# # attrs attribute for Tag
# print (soup.p.attrs)
# print (soup.p['class'])
# print (soup.p.get('class'))

# ## NavigableString
# print (soup.p.string)
# print (type(soup.p.string))

# ## BeautifulSoup
# print (type(soup.name))
# print (soup.name)
# print (soup.attrs)

# ## Comment 是一个特殊类型的NavigableString
# print (soup.a)
# if type(soup.a.string) == bs4.element.Comment:
#     print (soup.a.string)
# print (type(soup.a.string))



## 遍历文档树
# print (soup.head.contents)
# print (soup.head.children)
# for child in soup.body.children:
# 	print (child)
# for child in soup.descendants:
# 	print (child)
# for string in soup.strings:
# 	print (repr(string))
# for string in soup.stripped_strings:
# 	print (repr(string))

# print (soup.p.parent.name)    # 父节点
# content = soup.head.title.string    # 全部父节点
# for parent in content.parents:
# 	print (parent.name) 
# print (soup.p.next_sibling)    # 换行符
# print (soup.p.prev_sibling)
# print (soup.p.next_sibling.next_sibling)
# for sibling in soup.a.next_siblings:
# 	print (repr(sibling))



## 搜索文档树
# # find_all()
# print (type(soup.find_all('b')))    # name参数
# print (soup.find_all('b'))
# print (soup.find_all('a'))
# print (soup.find_all('b', 'a'))