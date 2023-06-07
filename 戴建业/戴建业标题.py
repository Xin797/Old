# 导入模块
import json
import requests

# 循环9次，将每一页的数据都抓取到
for i in range(1, 10):
    # 模拟浏览器
    headers = {
        'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    # 包含待爬取信息的url
    url = 'https://api.bilibili.com/x/space/arc/search?mid=532741557&&pn=%s&ps=30&jsonp=jsonp'%(i)

    # 访问url
    r = requests.get(url = url, headers = headers)
    # 将爬取到的json格式的数据转化为字典
    text = json.loads(r.text)
    # 取出嵌套字典里我们想要的部分
    res = text['data']['list']['vlist']
    for item in res:
        # 以列表的形式取出有用的数据
        list = ['av: ' + str(item['aid']), ' 视频标题: ' + item['title'], ' 播放量: ' + str(item['play']),
                ' 评论条数: ' + str(item['video_review'])]
        # 转化为字符串格式
        result = ''.join(list)
        # 写进文件里
        with open('戴建业标题.txt', 'a+', encoding="utf-8") as f:
            f.write(result + '\n')
