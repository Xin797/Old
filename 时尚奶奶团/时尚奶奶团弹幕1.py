import requests
import re

# 视频地址：

#请求网址
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=159520071'
#请求头
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'

}

f = open("时尚奶奶团弹幕1.txt", mode="w", encoding='utf-8')
# 发送请求
resp = requests.get(url=url, headers=headers)
#解决乱码
resp.encoding = 'utf-8'
# 解析数据
content_list = re.findall('<d p=".*?">(.*?)</d>', resp.text)
for content in content_list:
    f.write(content)
    f.write('\n')

f.close()

