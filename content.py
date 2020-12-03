# -*- coding: utf-8 -*-
import random
import requests
from config import *
from methods import *

x = '/Volumes/U盘/129/' # 输入文本
# Today_res = '/Users/lilong/Desktop/123/'
riyutuurl = '/Users/lilong/Desktop/likeshuo/url.txt'  # 图片
upan = '/Volumes/U盘/129_/'  # 输出文本
op_url = open(riyutuurl, encoding='utf-8')
pool_op_url = list(op_url)
df = res(x)
tt = df[0]
cc = df[1]
# print(cc[0])
i = 0
for t,c,tu_url in zip(tt,cc,pool_op_url):
    random.shuffle(pool_op_url)
    con_url = pool_op_url[0]
    # print(con_url)
    url = "<p style={center}><img src={url}  alt={rt}></p>".format(center="text-align:center", url=con_url, rt=t)  # 图片链接


    page = cc[i]
    i += 1
    list_page = page.split('\n')
    df = [x for x in list_page if x != '']
    # print(df)
    # for j in range(len(df)):j

    # 为每个自然段加上<p>
    l_p = []
    for j in range(len(df)):
        pi = '<p>' + df[j] + '</p>'
        # print(pi)
        strj = pi.replace('，免费试听课领取入口：https://www.nicekid.com/register/nicekid-jolene', '')
        strj = strj.replace('，试听课领取地址：','')

        l_p.append(strj)
    l_p.insert(0,url)
    del (l_p[-1])



    # print(l_p)
    # print(len(l_p))

    text = '\n'.join(l_p)

    Body = {'txt': text}  # 入参
    res_api = requests.post(url_num, headers=headers, data=Body)  # 接口调用
    resTest = json.loads(res_api.text)
    Test = resTest['data']

    t = t.replace('2015', '2020')
    tt = t.replace('2016','2020')
    ttt = tt.replace('2017', '2020')
    tttt = ttt.replace('2018', '2020')
    ttttt = tttt.replace('2019', '2020')

    Test1 = text.replace('2015', '2020')
    Test2 = Test1.replace('2016','2020')
    Test3 = Test2.replace('2017', '2020')
    Test4 = Test3.replace('2018', '2020')
    Test5 = Test4.replace('2019', '2020')
    # print(Test5)

    Txt_Create(upan, ttttt, Test5)
print('ok')
