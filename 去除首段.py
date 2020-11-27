from methods import *
clear_url = '/Users/lilong/Desktop/test/'
cl = '/Users/lilong/Desktop/123/'
df = res(clear_url)
tt = df[0]
cc = df[1]
i = 0
for t,c in zip(tt,cc):
    page = cc[i]
    i += 1
    list_page = page.split('\n')
    df = [x for x in list_page if x != '']
    df = df[2::]
    text = '\n'.join(df)
    Txt_Create(cl,t,text)




