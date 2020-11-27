from config import *
from methods import *
import random
x = '/Users/lilong/Desktop/cl/'
Today_res = '/Users/lilong/Desktop/123/'
riyutuurl = '/Users/lilong/Desktop/likeshuo/url.txt'
upan = '/Volumes/U盘/vv/'
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
    url = "<p style={center}><img src={url}  alt={rt}></p>".format(center="text-align:center", url=con_url, rt=t)  # 图片链


    page = cc[i]
    i += 1
    list_page = page.split('\n')
    df = [x for x in list_page if x != '']
    # print(df)
    # for j in range(len(df)):j
    l_p = []
    for j in range(len(df)):
        pi = '<p>' + df[j] + '</p>'
        # print(pi)
        l_p.append(pi)
    l_p.insert(0,url)
    # print(l_p)
    # print(len(l_p))
    text = '\n'.join(l_p)
    Txt_Create(upan, t, text)
