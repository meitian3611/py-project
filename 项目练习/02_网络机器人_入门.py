"""
网页解析:
lxml: 高性能的 HTML/XML的文档解析库,支持 Xpath 语法来解析和获取网页数据
Xpath: 一种在 HTML/XML中导航和定位元素的查询语言,可以精准的找到对应的元素 属性和文本
    /           从根节点的直接子元素       /html/bodu/div/h1
    //          从任意位置获取节点         //h1/text()
    [x]         选择第几个元素            p[3]
    [last()]    选择最后一个元素          p[last()]
    [@attr]     选择拥有指定属性的元素     p[@class]  p[@class="content]
    *           匹配任何元素节点          //body/div/*
    @*          匹配元素的任何属性        //body/div/a/@*
    text()      获取文本内容             //div/p/text()
"""

import requests
from lxml import html

# 定义URL
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求 获取数据
response = requests.get(target_url)
document = html.fromstring(response.text)

th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
tr_list = document.xpath("//table[@id='top20']/tbody/tr")

print(th_list)
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)