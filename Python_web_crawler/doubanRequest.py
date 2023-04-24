
# -*- coding: utf-8 -*-
# #!/usr/bin/python3

# 获取网页内容
import requests
#r = requests.get('https://book.douban.com/subject/27124847/?icn=index-topchart-subject').text
r = requests.get('https://book.douban.com/subject/1084336/comments/').text

# 使用BeautifulSoup4解析数据
# 需要安装第三方库beautufulSoup、lxml
# pip3 install BeautifulSoup4  lxml
from bs4 import BeautifulSoup
soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p','comment-content')
for item in pattern:
    print(item.string)

# 使用pandas保持数据
# 需要安装第三方库pandas
# pip3 install pandas
import pandas
comments = []
for item in pattern:
    comments.append(item.string)
df = pandas.DataFrame(comments)
# 直接导出会显示乱码，解决方法有两个：
# 方法一：指定编码方式 encoding = ‘utf-8-sig’
df.to_csv('commentsOfDouban.csv',encoding = 'utf-8-sig')
# 方法二：导出为xls文件。前提需要 pip3 install xlwt
# df.to_excel('commentsOfDouban.xls', index=False)
