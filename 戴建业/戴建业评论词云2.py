import jieba
import wordcloud
import numpy
from PIL import Image
import jieba.analyse

# 读取文件内容
f = open("戴建业评论2.txt", encoding='utf-8')
txt = f.read()

words  =  jieba.analyse.extract_tags(txt, topK=100, withWeight=False, allowPOS=('ns', 'n', 'vn','nr','a','v'))
wc = wordcloud.WordCloud(
    width = 700,
    height = 700,
    background_color = 'white',
    font_path = 'msyh.ttc',
    scale = 15,
)
wc.generate(str(words))
wc.to_file('戴建业评论词云2.png')

f.close()
