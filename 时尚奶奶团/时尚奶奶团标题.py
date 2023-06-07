# 导入模块
import json
import requests

# 视频只有两页 为了方便把不同页的url以列表的形式保存
# 模拟浏览器
for i in range(0,2):
    headers = {
        'User-Agent':  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    # 包含待爬取信息的url
    url = ['https://api.bilibili.com/x/space/wbi/arc/search?mid=53657202&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=3afe6326bcf3cf6f32ab95f09334bd93&wts=1685891296',
           'https://api.bilibili.com/x/space/wbi/arc/search?mid=53657202&ps=30&tid=0&pn=2&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=6a5f1d42c5fe8cc767a631c1045e3d7b&wts=1685891641']

    # 访问url
    r = requests.get(url = url[i], headers = headers)
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
        with open('时尚奶奶团标题.txt', 'a+', encoding="utf-8") as f:
            f.write(result + '\n')
