# -*- coding: utf-8 -*-
import random
import requests
from config import *
from methods import *

filename = input("文件名：")
g_url = '/Volumes/U盘/res/res'
x = g_url + '/{0}/'.format(filename)     # 输入文本
# Today_res = '/Users/lilong/Desktop/123/'
# upan = '/Volumes/U盘/00_/'  # 输出文本
filename1 = filename + '_'
y = g_url + '/{0}'.format(filename1)
Make_Folers_url(y)
y_ = y + '/'



# op_url = open(riyutuurl, encoding='utf-8')
# pool_op_url = list(op_url)
tp_url = input("en_url(e) or ri_url(r):")
pool_op_url = select(tp_url)

df = res(x)
tt = df[0]
cc = df[1]
# print(cc[0])k
i = 0
k = 0
for t,c in zip(tt,cc):
    k += 1
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
        strj = df[j].replace('，免费试听课领取入口：https://www.nicekid.com/register/nicekid-jolene', '')
        strj1 = strj.replace('，试听课领取地址：','')


        l_p.append(pi)
    l_p.insert(0,url)
    # del (l_p[-1])



    # print(l_p)
    # print(len(l_p))

    text = '\n'.join(l_p)

    Body = {'txt': text}  # 入参
    res_api = requests.post(url_num, headers=headers, data=Body)  # 接口调用
    resTest = json.loads(res_api.text)
    text = resTest['data']

    t = t.replace('15', '2020')
    tt = t.replace('16', '2020')
    ttt = tt.replace('17', '2020')
    tttt = ttt.replace('18', '2020')
    ttttt = tttt.replace('19', '2020')

    Test1 = text.replace('15', '2020')
    Test2 = Test1.replace('16', '2020')
    Test3 = Test2.replace('17', '2020')
    Test4 = Test3.replace('18', '2020')
    Test5 = Test4.replace('19', '2020')
    Test6 = Test5.replace('https://www.acadsoc.com.cn/lps/lp-tutor/mix-tutor.htm?search=','')
    Test7 = Test6.replace('acadsoc','likeshuo')
    Test8 = Test7.replace('阿卡索', '立刻说')

    # print(Test5)

    Txt_Create(y_, ttttt, Test8)
print('ok',k)
