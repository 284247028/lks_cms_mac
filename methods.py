import re
import json
import time
import random
import urllib
import codecs
import hashlib
import os, pprint
import urllib.parse, urllib.request
# likeshuo 方法
def TranslateBaidu(text, f='zh', t='en'):
    try:
        # 百度二次翻译，中-英-中
        appid = '20201014000589123'
        secretKey = '_Yfh1lzTWPDXytFhfYr2'
        url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = appid + text + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + 'zh' + '&to=' + 'en' + '&salt=' + str(
            salt) + '&sign=' + sign
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data["trans_result"][0]['dst'])
        time.sleep(1)   # 时间
        # 第二次翻译
        appid = '20201016000590625'
        secretKey = 'TW8AeSIyRwEeeIr5RSN4'
        url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = appid + result + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(
            result) + '&from=' + 'en' + '&to=' + 'zh' + '&salt=' + str(
            salt) + '&sign=' + sign
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data["trans_result"][0]['dst'])
        return result
    except:
        pass

def File_List(url):
    # 提供全链接，去除文本中的换行符;结果返回一个列表，每个段落装在字符串,整体装在列表，打印出来。
    file = open(url, encoding='utf-8')
    file = list(file)
    file = [x for x in file if x != '\n']
    # 如果要装在字符串中
    # str_file = ''.join(file)
    return file
# F = File_List('/Volumes/U盘/test/2.txt')
# print(F[2])
def Txt_Create(Target_Path,name, msg):
    # 新创建的txt文件的存放路径,需要提供url,生成文本及内容。msg是str。
    full_path = Target_Path + name + '.txt'  # 也可以创建一个.doc的word文档
    # Target_Path='/Volumes/U盘/test/'
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world
    file.close()
    return file

def File_Eli(path):
    # 剔除隐藏的文件,需要提供被测文件的路径，生成一个剔除隐藏文件后的列表。
    # path = '/Volumes/U盘/test/'
    path = os.listdir(path)
    ls = []
    for f in path:
        # print(f)
        if not f.startswith('.'):
            ls.append(f)
    return ls

def Read_File(Path,ls):
    # 提供path(路径)和ls(剔除隐藏文件的的列表)，能打印出列表文本中的内容
    # print("#"+Path,ls)
    file_content = []
    for i in range(len(ls)):
        url = Path + ls[i]
        f = open(url, encoding="utf-8")
        f = list(f)
        file_content.append(f)
    return file_content

# 生成文件夹
def Make_Folers(Target_Path,Dir_Name):
    # all_link = '/Users/lilong/Desktop/in/{}'.format(dir_name)
    # /Users/lilong/Desktop/
    Target_Link = Target_Path + Dir_Name
    Dir = os.makedirs(Target_Link)
    return Dir
# methods测试##
def random_sip(val,lsit1):  # 产生新列表，旧列表中插入值在随机位置、不在首尾,适合一维列表。
    lsit2 = [i for i in range(1,len(lsit1))]
    f = random.sample(lsit2,2)
    lsit1.insert(f[0],val)
    lsit1.insert(f[1],val)
    return lsit1

def list_list_sip(list_list,str1,str2):     # 输入参数是一个二维列表，两个不同的字符串
    def random_sip(val, lsit1):  # 产生新列表，旧列表中插入值在随机位置、不在首尾,适合一维列表。
        lsit2 = [i for i in range(1, len(lsit1))]
        f = random.sample(lsit2, 1)
        lsit1.insert(f[0], val)
        return lsit1
    out_list = [i for i in range(1,len(list_list))]
    sam = random.sample(out_list,2)
    one = list_list[sam[0]]
    random_sip(str1,one)
    two = list_list[sam[1]]
    random_sip(str2,two)
    return list_list

def res(res_url):  # 获取文件夹的名字和内容整体装在一个列表，返回值[0]tt [1]cc
    res = File_Eli(res_url)
    res_name = [i.replace('.txt', '') for i in res]
    tt = []
    cc = []
    for i in range(len(res_name)):
        tt.append(res_name[i])
        url = res_url + res_name[i] + '.txt'
        T_Conttent = File_List(url)
        str_W_Con = ''.join(T_Conttent)
        cc.append(str_W_Con)
    return tt, cc

# f = File_List('/Users/lilong/Desktop/res/零基础学日语：五十音听读写训练 22.txt')
# # print(f)
# a = TranslateBaidu('')
# print(a)

