import requests
import time
import re
se = requests.session()



if __name__ == '__main__':
    text = '''
其实我也是研究了很久关于线上英语培训机构的事情了，hualongyey也去问了很多人的意见      我们在生活中常常会发生好多事,而在这其中我们难免会遇到心情不好的时候,下面小编为大家整理的感到沮丧的英语口语对话，希望对大家有用!    感到沮丧的英语口语对话  A: Joyce, have you noticed my poor manner in the presentation?  B: You were completely confident. What happened?  A: You didnt see my un所以都卯足了劲给孩子就给孩子找靠的cxsxsl少儿英语培训英语启蒙了ease?  B: No! Until half-way, you suddenly became unsure of yourself.  A: Yes. It is because of Mr. Wang.  B: What about him?  A: He seems not to be a gentleman, reading his files instead of showing a little bit respect to me.  B: Did you try to ignore that?  A: I tried to ignore his impoliteness, but I failed.  B: Did Mr. Wang do anything else?  A: He is also spinning the chair and looking out the window constantly.  B: Try not to let this upset you too much.  A: Thank you for being so sweet.  B: You are welcome.  A：乔伊斯，你看到我做报告的时候表现很糟糕了吗?  B：你当时很自信啊，怎么了?  A：你没发现我很不自在吗?  B：没有，但中途你突然就变得不自信了。  A：是的。是因为那个王先生。  B：他怎么了?  A：他一点都不绅士，一直在看他自己的文件，一点也不尊重我。  B：你有试着转移注意力吗?  A：有的，只是失败了。  B：他还有做其他的动作吗?  A：是的，他一直在转他的椅子而且眼睛老看着窗外。  B：不要因为这个太沮丧了。  A：谢谢你这么体贴。  B：没关系。 
'''
    Post_url = "http://api-11.78tp.com/api.php?json=0&v=1&key=aa952816267"
    Post_data = {
        'wenzhang': text
    }
    Text = se.post(Post_url, data=Post_data).text
    print(Text)