import requests
import re

# 视频地址：https://www.bilibili.com/video/BV1oq4y1N7oG/?spm_id_from=333.337.search-card.all.click&vd_source=839e8de2456c5813b619aa0212a714e5

#请求网址
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=405675007'

#请求头
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.197.400 QQBrowser/11.7.5287.400'}

f = open("戴建业弹幕2.txt", mode="w", encoding='utf-8')
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

