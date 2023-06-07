import jieba
import wordcloud

# 读取文件内容
f = open("戴建业弹幕2.txt", encoding ='utf-8')
txt = f.read()
string = ' '.join(jieba.lcut(txt))
char_to_remove1 = "的"
char_to_remove2 = "哈"

string1 = string.replace(char_to_remove1, "")
string2 = string1.replace(char_to_remove2, "")
wc = wordcloud.WordCloud(
    width = 700,
    height = 700,
    background_color = 'white',
    font_path = 'msyh.ttc',
    scale = 15,
)
wc.generate(string2)
wc.to_file('戴建业弹幕2.png')

f.close()