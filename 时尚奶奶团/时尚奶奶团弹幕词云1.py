import jieba
import wordcloud
import jieba.analyse

# 读取文件内容
f = open("时尚奶奶团弹幕1.txt", encoding ='utf-8')
txt = f.read()
string = ' '.join(jieba.lcut(txt))

'''
char_to_remove1 = "的"
char_to_remove2 = "哈"
char_to_remove3 = "了"

string1 = string.replace(char_to_remove1, "")
string2 = string1.replace(char_to_remove2, "")
'''

words  =  jieba.analyse.extract_tags(txt, topK=100, withWeight=False, allowPOS=('ns', 'n', 'vn','nr','a','v'))

wc = wordcloud.WordCloud(
    width = 700,
    height = 700,
    background_color = 'white',
    font_path = 'msyh.ttc',
    scale = 15,
)
wc.generate(str(words))
wc.to_file('时尚奶奶团弹幕1词云plus.png')

f.close()