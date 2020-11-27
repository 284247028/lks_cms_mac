from methods import *
clear_url = '/Users/lilong/Desktop/test/'
df = res(clear_url)
tt = df[0]
cc = df[1]
# print(tt)
# print(cc)
page = cc[0]
# print(page)
list_page = page.split('\n')

df = [x for x in list_page if x != '']
print(df)
# print(df)
l_p = []
for i in df:
    pi = '<p>' + i + '</p>'
    l_p.append(pi)
str_txt = ''.join(l_p)
print(str_txt)
