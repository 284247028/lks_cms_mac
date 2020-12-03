# -*- coding: utf-8 -*-
import random
import requests
from config import *
from methods import *

x = '/Volumes/U盘/1000p_日语/' # 输入文本
# Today_res = '/Users/lilong/Desktop/123/'
riyutuurl = '/Users/lilong/Desktop/likeshuo/url.txt'  # 图片
upan = '/Volumes/U盘/riyu500_/'  # 输出文本
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
        # pi = '<p>' + df[j] + '</p>'
        # print(pi)
        strj = df[j].replace('，免费试听课领取入口：https://www.nicekid.com/register/nicekid-jolene', '')
        strj = strj.replace('，试听课领取地址：','')

        l_p.append(strj)
    l_p.insert(0,url)


    # print(l_p)
    # print(len(l_p))

    text = '\n'.join(l_p)

    Body = {'txt': text}  # 入参
    res_api = requests.post(url_num, headers=headers, data=Body)  # 接口调用
    resTest = json.loads(res_api.text)
    Test = resTest['data']

    Txt_Create(upan, t, Test)
print('ok')
