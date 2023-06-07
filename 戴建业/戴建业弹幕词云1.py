import jieba
import wordcloud
import numpy
from PIL import Image
import jieba.analyse

# 读取文件内容
f = open("戴建业弹幕1.txt", encoding='utf-8')
txt = f.read()
mask = numpy.array(Image.open('戴建业素材1.jpg'))

words  =  jieba.analyse.extract_tags(txt, topK=100, withWeight=False, allowPOS=('ns', 'n', 'vn','nr','a','v'))
wc = wordcloud.WordCloud(
    width = 700,
    height = 700,
    background_color = 'white',
    font_path = 'msyh.ttc',
    scale = 15,
    mask = mask,
)
wc.generate(str(words))
wc.to_file('戴建业弹幕1.png')

f.close()
