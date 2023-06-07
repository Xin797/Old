import requests
import re

#请求网址
url = ['https://api.bilibili.com/x/v1/dm/list.so?oid=384102076','https://api.bilibili.com/x/v1/dm/list.so?oid=204939635',
       'https://api.bilibili.com/x/v1/dm/list.so?oid=345188905','https://api.bilibili.com/x/v1/dm/list.so?oid=351918690',
       'https://api.bilibili.com/x/v1/dm/list.so?oid=203760532','https://api.bilibili.com/x/v1/dm/list.so?oid=218463847',
       'https://api.bilibili.com/x/v1/dm/list.so?oid=248007988','https://api.bilibili.com/x/v1/dm/list.so?oid=878557878',
       'https://api.bilibili.com/x/v1/dm/list.so?oid=985494074','https://api.bilibili.com/x/v1/dm/list.so?oid=220717516'
]

#请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

f = open("戴建业弹幕1.txt", mode="w", encoding='utf-8')
for i in range(10):
    # 发送请求
    resp = requests.get(url=url[i], headers=headers)
    #解决乱码
    resp.encoding = 'utf-8'
    # 解析数据
    content_list = re.findall('<d p=".*?">(.*?)</d>', resp.text)
    for content in content_list:
        f.write(content)
        f.write('\n')

f.close()





