# res_url = '/Volumes/U盘/A20201127/'
# 资源文件夹
from methods import *
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'A5F46DD7D7F1442D928B1DCE068B38A7'}#消息头，根据实际需要添加
url_num = "http://apis.5118.com/wyc/akey"  #地址
riyutuurl = '/Users/lilong/Desktop/likeshuo/lks_url_riyu.txt'
enyutuurl = '/Users/lilong/Desktop/likeshuo/lks_url_en.txt'
op_url = open(riyutuurl, encoding='utf-8')
pool_op_url = list(op_url)

# www.shkqn.com/Little
isojb = 'www.isojb.net/Little'
bohansd = 'www.bohansd.com/Little'
weimin110 = 'www.weimin110.net/Little'
fygov = 'www.fygov.cn/Little'
shkqn = 'www.shkqn.com/Little'
ymschoolmj = 'www.ymschoolmj.com/Little'



isojb_url = 'http://' + isojb
bohansd_url = 'http://' + bohansd
weimin110_url = 'http://' + weimin110
fygov_url = 'http://' + fygov
shkqn_url = 'http://' + shkqn
ymschoolmj_url = 'http://' + ymschoolmj


def select(i):
    global pool_op_url
    if i == 'r':
        op_urlr = open(riyutuurl, encoding='utf-8')
        pool_op_url = list(op_urlr)
        # print(pool_op_url)

    elif i == 'e':
        op_urle = open(enyutuurl, encoding='utf-8')
        pool_op_url = list(op_urle)
        # print(pool_op_url)

    else:
        print("输入有误")
    return pool_op_url


