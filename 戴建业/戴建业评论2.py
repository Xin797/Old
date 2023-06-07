# 爬取评论

import requests

f = open('戴建业评论2.txt', mode ='w', encoding='utf-8')

for i in range(1,12):
    page = str(i)
    url = 'https://api.bilibili.com/x/v2/reply/main?csrf=a7974b634c8ce08aeb9541999bf2c0f8&mode=3&oid=547993469&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:1,%5C%22direction%5C%22:1,%5C%22data%5C%22:%7B%5C%22pn%5C%22:' + page + '%7D%7D%22%7D&plat=1&type=1'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, headers=headers)

    for index in response.json()['data']['replies']:
        content = index['content']['message']
        f.write(content)
        f.write('\n')
f.close()





