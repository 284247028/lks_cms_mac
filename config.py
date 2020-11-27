res_url = '/Volumes/U盘/A20201127/'     # 资源文件夹
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'A5F46DD7D7F1442D928B1DCE068B38A7'}#消息头，根据实际需要添加
url_num = "http://apis.5118.com/wyc/akey"  #地址
riyutuurl = '/Users/lilong/Desktop/likeshuo/url.txt'
op_url = open(riyutuurl, encoding='utf-8')
pool_op_url = list(op_url)

# www.shkqn.com/Little
shkqn = 'www.shkqn.com/Little'
shkqn_url = 'http://' + shkqn