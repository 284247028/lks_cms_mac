from methods import *
clear_url = '/Volumes/U盘/work_test/'
cl = '/Volumes/U盘/work_on/'
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

    Body = {'txt': text}  # 入参
    res_api = requests.post(url_num, headers=headers, data=Body)  # 接口调用
    resTest = json.loads(res_api.text)
    Test = resTest['data']

    Txt_Create(cl,t,Test)




